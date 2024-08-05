"""Module to convert restructured text to html in markdown."""

import warnings

from markdown import Markdown
from markdown.extensions.attr_list import get_attrs_and_remainder
from markdown.extensions.fenced_code import FencedBlockPreprocessor
from markdown.preprocessors import Preprocessor

from rst_in_md.conversion import BS4_FORMATTER, LANGUAGES, rst_to_soup


class RestructuredTextInMarkdownPreProcessor(Preprocessor):
    """Preprocessor to convert restructured text to html in markdown."""

    _Processor = FencedBlockPreprocessor(Markdown(), {})
    FENCED_BLOCK_RE = _Processor.FENCED_BLOCK_RE
    handle_attrs = _Processor.handle_attrs

    def run(self, lines: list[str]) -> list[str]:
        """Strip restuctured text from markdown and replace it with converted html.

        This method will look for fenced code blocks in markdown that are marked as
        restructured text (`rst`, `rest`, `restructuredtext`) and convert them to html.
        It leverages the same regex as the [FencedBlockPreprocessor](https://github.com/Python-Markdown/markdown/blob/33359faa385f59b84cd87df5f4b0996055a482e2/markdown/extensions/fenced_code.py#L56-L67)
        to find the blocks.

        You can also add an ignore comment right before the fenced block to prevent it
        from being converted. The comment should be `<!-- ignore: rst-in-md -->`. You
        can see an example of this [here](../guides/inline_ignore.md).

        Args:
            lines (list[str]): List of lines in markdown.

        Returns:
            list[str]: List of lines in markdown with rst replaced with html.
        """
        text = "\n".join(lines)
        processed = ""
        index = 0
        for match in self.FENCED_BLOCK_RE.finditer(text):
            lang = None
            attrs = []
            classes = []
            config = {}
            if match.group("lang") is not None:
                lang = match.group("lang")
            elif match.group("attrs") is not None:
                attrs, remainder = get_attrs_and_remainder(match.group("attrs"))
                if remainder:  # skip this match due to invalid syntax
                    warnings.warn("Invalid syntax parsing attributes", stacklevel=1)
                    processed += text[match.start() : match.end()]
                    index = match.end()
                    continue
                _, classes, config = self.handle_attrs(attrs)
                if len(classes) > 0:
                    lang = classes.pop(0)

            processed += text[index : match.start()]

            if lang not in LANGUAGES or config.get("rst-in-md") == "false":
                processed += text[match.start() : match.end()]
            else:
                try:
                    processed += rst_to_soup(match.group("code")).prettify(
                        formatter=BS4_FORMATTER,
                    )
                except ValueError as e:
                    warnings.warn(str(e), stacklevel=1)
                    processed += text[match.start() : match.end()]

            index = match.end()
        processed += text[index:]
        return processed.split("\n")
