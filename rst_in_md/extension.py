"""The RestructuredTextInMarkdown extension."""

from markdown import Extension, Markdown

from rst_in_md.processor import RestructuredTextInMarkdownPreProcessor
from rst_in_md.superfence import RestructuredTextInMarkdownAutoConfigurator


class RestructuredTextInMarkdown(Extension):
    """Extension to convert restructured text to html in markdown."""

    @staticmethod
    def _pymdownx_installed() -> bool:
        try:
            import pymdownx.superfences  # noqa: F401
        except ImportError:
            return False
        return True

    def extendMarkdown(self, md: Markdown) -> None:  # noqa: N802
        """Register the RestructuredTextInMarkdownPreProcessor.

        Register the
        [RestructuredTextInMarkdownPreProcessor](extension.md#rst_in_md.RestructuredTextInMarkdownPreProcessor)
        with the markdown instance. This allows the preprocessor to be used when
        markdown is rendered to html.

        The priority of the preprocessor is set to `27`. This is higher than
        the [fenced_code_block](https://github.com/Python-Markdown/markdown/blob/33359faa385f59b84cd87df5f4b0996055a482e2/markdown/extensions/fenced_code.py#L50)
        preprocessor, so that `rst` blocks are processed beforehand. But it is
        lower than [normalize_whitespace](https://github.com/Python-Markdown/markdown/blob/33359faa385f59b84cd87df5f4b0996055a482e2/markdown/preprocessors.py#L40)
        so that the rst blocks can be processed in a similar manner to code blocks.

        Also register the
        [RestructuredTextInMarkdownAutoConfigurator](superfence.md#rst_in_md.RestructuredTextInMarkdownAutoConfigurator)
        if `pymdownx.superfences` is installed.

        Args:
            md (Markdown): The Markdown instance.
        """
        md.preprocessors.register(
            RestructuredTextInMarkdownPreProcessor(md),
            "rst-in-md",
            27,
        )

        if self._pymdownx_installed():
            md.preprocessors.register(
                RestructuredTextInMarkdownAutoConfigurator(md),
                "rst-in-md-auto-configurator",
                300,
            )
