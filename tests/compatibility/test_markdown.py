from textwrap import dedent

import pytest
from markdown import Markdown

from rst_in_md import RestructuredTextInMarkdownPreProcessor


@pytest.fixture()
def md():
    return Markdown(extensions=["rst_in_md", "fenced_code", "attr_list"])


def test_load_extension(md):
    converted = md.convert(source=(source := ""))
    assert source == converted

    assert any(
        isinstance(p, RestructuredTextInMarkdownPreProcessor) for p in md.preprocessors
    )


def test_higher_priority_than_html_block(md):
    rst_index = md.preprocessors.get_index_for_name("rst-in-md")
    html_index = md.preprocessors.get_index_for_name("html_block")
    assert rst_index < html_index


def test_higher_priority_than_fenced_code(md):
    rst_index = md.preprocessors.get_index_for_name("rst-in-md")
    fenced_code_index = md.preprocessors.get_index_for_name("fenced_code_block")
    assert rst_index < fenced_code_index


def test_fenced_code_blocks(md):
    languages = [
        "rst",
        "rest",
        "restructuredtext",
        "{.rst}",
        "{.rest}",
        "{.restructuredtext}",
        "{.rst attr=value}",
        "{ .rst }",
        "{ .rst attr=value }",
    ]
    for lang in languages:
        source = dedent(f"""
        ```{lang}
        test
        ```
        """).strip("\n")
        assert md.convert(source=source) == "<p>\n  test\n</p>"


def test_ignore_rst_in_md(md):
    source = dedent("""
    ```{.rst rst-in-md=false}
    Section to ignore
    ```
    """).strip("\n")
    assert (
        md.convert(source=source)
        == '<pre><code class="language-rst" rst-in-md="false">Section to ignore\n</code></pre>'  # noqa: E501
    )
