"""PyMdown Extensions Custom Superfence for `rst_in_md`."""

import logging

from markdown import Markdown
from markdown.preprocessors import Preprocessor
from pymdownx.superfences import SuperFencesBlockPreprocessor

from rst_in_md.conversion import BS4_FORMATTER, LANGUAGES, rst_to_soup

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class Configurator(Preprocessor):
    """Preprocessor to deregister `rst-in-md` if `pymdownx.superfences` is installed."""

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

    def run(self, lines: list[str]) -> list[str]:
        """Deregister `rst-in-md` if `pymdownx.superfences` is installed.

        Args:
            lines (list[str]): Input lines _(required, but not used)_.

        Returns:
            list[str]: Identical as the input lines.
        """
        if not self.initialized and self.superfences_installed():
            self.md.preprocessors.deregister("rst-in-md")
            self.initialized = True

        return lines


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

    !!! note
        This function is passed a few arguments that are not used. They are required by
        `pymdownx.superfences`.

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
