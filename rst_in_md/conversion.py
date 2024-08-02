"""Module for converting restructured text to html in a markdown compatible manner."""

import io
from contextlib import redirect_stderr

import docutils.core
from bs4 import BeautifulSoup, Tag, formatter

ATTRIBUTES_TO_STRIP = ["class", "id", "name", "style", "border"]
BS4_FORMATTER = formatter.HTMLFormatter(indent=2)


def _rst_to_soup(rst: str) -> BeautifulSoup:
    """Convert reStructuredText to a BeautifulSoup object.

    This will convert the reStructuredText to HTML using docutils. The HTML is then
    converted to a BeautifulSoup object and returned.

    Errors and warnings are captured gracefully and raised at the end.

    This function is heavily inspired by this [rst2html](https://github.com/andrewpetrochenkov/rst2html.py/blob/b66942f16e93d7260748ecc90867c55a4bb3236d/rst2html/__init__.py)
    implementation.

    Args:
        rst (str): The reStructuredText to convert.

    Raises:
        ValueError: If there are any errors or warnings during the conversion.

    Returns:
        BeautifulSoup: The converted reStructuredText.
    """
    kwargs = {
        "writer_name": "html",
        "settings_overrides": {
            "_disable_config": True,
            "report_level": 2,
        },
    }

    with io.StringIO() as target, redirect_stderr(target):
        parts = docutils.core.publish_parts(rst, **kwargs)
        warning = target.getvalue().strip()

    if warning:
        msg = f"Failed to convert restructured text:\n\n{warning}"
        raise ValueError(msg)

    return BeautifulSoup(parts.get("body"), features="html.parser")


def _strip_attributes(soup: BeautifulSoup) -> BeautifulSoup:
    """Remove specific attributes from the soup.

    This will remove all attributes from the top level tags, and will also remove
    some attributes from the descendants. This took heavy inspiration from this
    [StackOverflow answer](https://stackoverflow.com/a/9045719).

    Args:
        soup (BeautifulSoup): Input soup to remove attributes from.

    Returns:
        BeautifulSoup: Same soup with attributes removed.
    """
    # Remove attributes from the top level tags
    for tag in soup.contents:
        if isinstance(tag, Tag):
            tag.attrs = {}

    # Remove specific attributes from the descendants
    for tag in soup.descendants:
        if isinstance(tag, Tag):
            tag.attrs = {
                key: value
                for key, value in tag.attrs.items()
                if key not in ATTRIBUTES_TO_STRIP
            }
    return soup


def rst_to_soup(rst: str) -> BeautifulSoup:
    """Convert restructured text to html in a manner that is compatible with markdown.

    Args:
        rst (str): Raw restructured text to convert to html.

    Returns:
        str: Html converted from restructured text.
    """
    soup = _rst_to_soup(rst)
    return _strip_attributes(soup)
