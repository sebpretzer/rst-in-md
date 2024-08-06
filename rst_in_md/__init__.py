"""This module is the entry point for the RestructuredTextInMarkdown extension."""

from markdown.extensions import Extension

from rst_in_md.conversion import rst_to_soup
from rst_in_md.extension import RestructuredTextInMarkdown
from rst_in_md.processor import RestructuredTextInMarkdownPreProcessor
from rst_in_md.superfence import (
    RestructuredTextInMarkdownAutoConfigurator,
    superfence_formatter,
    superfence_validator,
)

__all__ = [
    "rst_to_soup",
    "RestructuredTextInMarkdown",
    "RestructuredTextInMarkdownPreProcessor",
    "RestructuredTextInMarkdownAutoConfigurator",
    "superfence_formatter",
    "superfence_validator",
]

__version__ = "0.0.0"


def makeExtension(**kwargs) -> Extension:  # noqa: N802, ANN003
    """Return an instance of the RestructuredTextInMarkdown extension.

    This function is specified by the markdown package, so that it can properly load the
    extension. You can find more information about this function in the [markdown documentation](https://python-markdown.github.io/extensions/api/#dot_notation).

    Returns:
        Extension: An instance of the RestructuredTextInMarkdown extension.
    """
    return RestructuredTextInMarkdown(**kwargs)
