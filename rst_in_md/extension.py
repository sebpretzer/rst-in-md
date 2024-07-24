"""The RestructuredTextInMarkdown extension."""

from markdown import Extension, Markdown

from rst_in_md.processor import RestructuredTextInMarkdownPreProcessor


class RestructuredTextInMarkdown(Extension):
    """Extension to convert restructured text to html in markdown."""

    def extendMarkdown(self, md: Markdown) -> None:  # noqa: N802
        """Register the RestructuredTextInMarkdownPreProcessor.

        Register the RestructuredTextInMarkdownPreProcessor with the markdown instance.
        This allows the preprocessor to be used when markdown is rendered to html. It
        will have a higher priority than `markdown.preprocessors.HtmlBlockPreprocessor`,
        so that rst blocks are not processed as html blocks. The priorities can be found
        in the [markdown.preprocessors module](https://github.com/Python-Markdown/markdown/blob/33359faa385f59b84cd87df5f4b0996055a482e2/markdown/preprocessors.py#L40-L41).


        Args:
            md (Markdown): The Markdown instance.
        """
        md.preprocessors.register(
            RestructuredTextInMarkdownPreProcessor(md),
            "rst-in-md",
            27,
        )
