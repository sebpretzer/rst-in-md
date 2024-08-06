"""PyMdown Extensions Custom Superfence for `rst_in_md`."""

import logging
from functools import partial

from markdown import Markdown
from markdown.preprocessors import Preprocessor
from pymdownx.superfences import (
    SuperFencesBlockPreprocessor,
    SuperFencesCodeExtension,
    _formatter,
    _test,
    _validator,
)

from rst_in_md.conversion import BS4_FORMATTER, LANGUAGES, rst_to_soup

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def superfence_formatter(
    source: str,
    language: str,  # noqa: ARG001
    css_class: str,  # noqa: ARG001
    options: dict,  # noqa: ARG001
    md: Markdown,  # noqa: ARG001
    **kwargs: dict,  # noqa: ARG001
) -> str:
    """Convert superfenced reStructuredText to html.

    This function will convert the reStructuredText to html using the same method as
    the standard python markdown extension.

    !!! note "Unused Arguments"
        This function is passed a few arguments that are not used. It must adhere to
        [the required signature](https://facelessuser.github.io/pymdown-extensions/extensions/superfences/#formatters)
        set by `pymdownx.superfences`.

    Args:
        source (str): Language of the superfence.
        language (str): Language of the superfence _(required, but not used)_.
        css_class (str): CSS class of the superfence _(required, but not used)_.
        options (dict): Options of the superfence _(required, but not used)_.
        md (Markdown): The markdown instance _(required, but not used)_.
        **kwargs (dict): Additional arguments _(required, but not used)_.

    Returns:
        str: The converted html.
    """
    return rst_to_soup(source).prettify(formatter=BS4_FORMATTER)


def superfence_validator(
    language: str,
    inputs: dict,
    options: dict,
    attrs: dict,
    md: Markdown,  # noqa: ARG001
) -> bool:
    """Validate that the superfence should be processed.

    This function will validate that the superfence should be processed by `rst-in-md`.
    This includes:

    * Checking if the language is supported.
    * Checking if the `rst-in-md` attribute is set to `false` or not.
    * Checking if any options or attributes are passed.

    !!! note "Unused Arguments"
        `md` is passed to this function but is not used. It must adhere to
        [the required signature](https://facelessuser.github.io/pymdown-extensions/extensions/superfences/#validators)
        set by `pymdownx.superfences`.

    Args:
        language (str): Language of the superfence.
        inputs (dict): All the parsed options/attributes of the superfence.
        options (dict): A dictionary to which all valid options should be assigned to.
        attrs (dict): A dictionary to which all valid attributes should be assigned to.
        md (Markdown): the markdown instance _(required, but not used)_.

    Returns:
        bool: If the superfence should be processed or not.
    """
    if language not in LANGUAGES:
        msg = f"language '{language}' is not supported."
        logging.error(msg)
        return False

    allowed = {"rst-in-md"}
    if (keys := set(inputs.keys())) > allowed:
        msg = f"keys '{keys - allowed}' are not supported."
        logging.error(msg)
        return False

    if inputs.get("rst-in-md") == "false":
        logging.info("rst-in-md is set to false.")
        return False

    if len(options) > 0:
        logging.error("options are not supported.")
        return False

    if len(attrs) > 0:
        logging.error("attrs are not supported.")
        return False

    return True


class RestructuredTextInMarkdownAutoConfigurator(Preprocessor):
    """Preprocessor to adapt `rst-in-md` to work with `pymdownx.superfences`."""

    initialized = False

    def superfences_installed(self) -> bool:
        """Check if the `pymdownx.superfences` extension is installed.

        Returns:
            bool: If the extension is installed or not.
        """
        return isinstance(
            self.md.preprocessors["fenced_code_block"],
            SuperFencesBlockPreprocessor,
        )

    @staticmethod
    def construct_fence_config(language: str) -> dict:
        """Create a fence configuration dictionary for `pymdownx.superfences`.

        Create a fence configuration for `pymdownx.superfences` with the given language,
        in the given [structure](https://github.com/facelessuser/pymdown-extensions/blob/cd7c704487a3a79b6619bfcd0c6af83104d630a8/pymdownx/superfences.py#L273-L276).
        This configuration will be read by `pymdownx.superfences` to determine how to
        process the superfence.

        Args:
            language (str): Language of the superfence.

        Returns:
            dict: Dictionary of the fence configuration.
        """
        return {
            "name": language,
            "class": "rst-in-md",
            "format": superfence_formatter,
            "validator": superfence_validator,
        }

    @staticmethod
    def construct_superfence(language: str) -> dict:
        """Create a superfence dictionary for `pymdownx.superfences`.

        Create a superfence dict for `pymdownx.superfences` with the given language,
        in the given [structure](https://github.com/facelessuser/pymdown-extensions/blob/cd7c704487a3a79b6619bfcd0c6af83104d630a8/pymdownx/superfences.py#L240-L245).
        This dictionary will be appended to `SuperFencesCodeExtension().superfences`.

        Args:
            language (str): Language of the superfence.

        Returns:
            dict: Dictionary of the superfence for `pymdownx.superfences`.
        """
        return {
            "name": language,
            "test": partial(_test, test_language=language),
            "formatter": partial(
                _formatter,
                class_name="rst-in-md",
                _fmt=superfence_formatter,
            ),
            "validator": partial(
                _validator,
                validator=superfence_validator,
            ),
        }

    def inject_custom_configs(self) -> None:
        """Add custom fence configs to `pymdownx.superfences`, if not already present.

        Raises:
            ValueError: SuperFencesCodeExtension not found.
        """
        registered = self.md.registeredExtensions
        extensions = [e for e in registered if isinstance(e, SuperFencesCodeExtension)]
        if len(extensions) != 1:
            msg = "Unable to find SuperFencesCodeExtension."
            raise ValueError(msg)
        ext = extensions[0]

        config = self.md.preprocessors["fenced_code_block"].config  # pyright: ignore[reportAttributeAccessIssue]
        custom_fences = config.get("custom_fences", [])
        for language in LANGUAGES:
            if (fence := self.construct_fence_config(language)) not in custom_fences:
                custom_fences.append(fence)
                ext.superfences.append(self.construct_superfence(language))

        config["custom_fences"] = custom_fences

    def run(self, lines: list[str]) -> list[str]:
        """Auto-configure `pymdownx.superfences` if installed.

        This method will check if `pymdownx.superfences` is installed. If it is, it will
        deregister `rst-in-md`, since `pymdownx.superfences` will handle the fenced code
        blocks. It will also provide the custom fence configurations needed for
        `pymdownx.superfences` to properly process the fenced code.

        !!! question "Why is this a preprocessor?"

            This preprocessor will not actually process any markdown, even if it is
            called for each markdown file. It much be run after all extensions have been
            initialized.

        Args:
            lines (list[str]): Input lines _(required, but not used)_.

        Returns:
            list[str]: Identical as the input lines.
        """
        if not self.initialized and self.superfences_installed():
            self.md.preprocessors.deregister("rst-in-md")
            self.inject_custom_configs()
            self.initialized = True

        return lines
