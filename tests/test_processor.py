from textwrap import dedent

import pytest

from rst_in_md import RestructuredTextInMarkdownPreProcessor


@pytest.fixture()
def preprocessor():
    return RestructuredTextInMarkdownPreProcessor()


def test_run(preprocessor):
    unprocessed = dedent("""
    ```rst
    Section 1
    ```

    Not rst

    ```restructuredtext
    Section 2
    ```

    Not restructuredtext

    ```rest
    Section 3
    ```

    Not rest
    """).strip("\n")

    processed = "\n".join(preprocessor.run(lines=unprocessed.split("\n")))

    for i in range(1, 4):
        assert f"<p>\n  Section {i}\n</p>" in processed
