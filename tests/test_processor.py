from textwrap import dedent


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


def test_ignore(preprocessor):
    unprocessed = dedent("""

    ```rst
    Section to convert
    ```

    <!-- ignore: rst-in-md -->
    ```rst
    Section to ignore
    ```

    """).strip("\n")

    processed = "\n".join(preprocessor.run(lines=unprocessed.split("\n")))

    assert "<p>\n  Section to convert\n</p>" in processed
    assert "```rst\nSection to ignore\n```" in processed
