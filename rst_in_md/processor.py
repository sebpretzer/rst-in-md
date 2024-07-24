"""Module to convert restructured text to html in markdown."""

import re
import warnings

import bs4
from markdown import Markdown
from markdown.extensions.fenced_code import FencedBlockPreprocessor
from markdown.preprocessors import Preprocessor

from rst_in_md.conversion import rst_to_soup


class RestructuredTextInMarkdownPreProcessor(Preprocessor):
    """Preprocessor to convert restructured text to html in markdown."""

    BS4_FORMATTER = bs4.formatter.HTMLFormatter(indent=2)
    # https://github.com/Python-Markdown/markdown/blob/33359faa385f59b84cd87df5f4b0996055a482e2/markdown/extensions/fenced_code.py#L56-L67
    FENCED_BLOCK_RE = FencedBlockPreprocessor(Markdown(), {}).FENCED_BLOCK_RE
    IGNORE_RE = re.compile(r"<!--\s*ignore:\s*rst-in-md\s*-->\s*$")

    def run(self, lines: list[str]) -> list[str]:
        """Strip restuctured text from markdown and replace it with converted html.

        This method will look for fenced code blocks in markdown that are marked as
        restructured text (`rst`, `rest`, `restructuredtext`) and convert them to html.
        It leverages the same regex as the `FencedBlockPreprocessor` to find the blocks.

        You can also add an ignore comment right before the fenced block to prevent it
        from being converted. The comment should be `<!-- ignore: rst-in-md -->`.

        Args:
            lines (list[str]): List of lines in markdown.

        Returns:
            list[str]: List of lines in markdown with rst replaced with html.
        """
        text = "\n".join(lines)
        processed = ""
        index = 0
        for match in self.FENCED_BLOCK_RE.finditer(text):
            processed += text[index : match.start()]

            if match.group("lang") not in ["rst", "rest", "restructuredtext"] or (
                self.IGNORE_RE.search(text[index : match.start()])
            ):
                processed += text[match.start() : match.end()]
            else:
                try:
                    processed += rst_to_soup(match.group("code")).prettify(
                        formatter=self.BS4_FORMATTER,
                    )
                except ValueError as e:
                    warnings.warn(str(e), stacklevel=1)
                    processed += text[match.start() : match.end()]

            index = match.end()
        processed += text[index:]
        return processed.split("\n")
