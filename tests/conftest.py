import pytest
from markdown import Markdown

from rst_in_md import RestructuredTextInMarkdownPreProcessor


@pytest.fixture()
def md():
    return Markdown(extensions=["rst_in_md", "fenced_code"])


@pytest.fixture()
def preprocessor():
    return RestructuredTextInMarkdownPreProcessor()
