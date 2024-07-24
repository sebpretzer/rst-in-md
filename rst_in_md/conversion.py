"""Module for converting restructured text to html in a markdown compatible manner."""

import io
from contextlib import redirect_stderr

import docutils.core
from bs4 import BeautifulSoup, Tag

ATTRIBUTES_TO_STRIP = ["class", "id", "name", "style"]


# https://github.com/andrewpetrochenkov/rst2html.py/blob/master/rst2html/__init__.py
def _rst_to_soup(rst: str) -> BeautifulSoup:
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


# https://stackoverflow.com/a/9045719
def _strip_attributes(soup: BeautifulSoup) -> BeautifulSoup:
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
