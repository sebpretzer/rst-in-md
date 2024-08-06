from textwrap import dedent

import pytest
from markdown import Markdown

from rst_in_md import superfence_formatter, superfence_validator


@pytest.fixture()
def md():
    return Markdown(
        extensions=[
            "rst_in_md",
            "admonition",
            "attr_list",
            "pymdownx.superfences",
        ],
        extension_configs={
            "pymdownx.superfences": {
                "custom_fences": [
                    {
                        "name": "rst",
                        "class": "rst-in-md",
                        "format": superfence_formatter,
                        "validator": superfence_validator,
                    },
                ],
            },
        },
    )


def test_load_extension_with_pymdownx(md):
    assert md.preprocessors.get_index_for_name("rst-in-md-configurator") == 0
    assert md.preprocessors["rst-in-md"]

    md.convert(source="placeholder")

    with pytest.raises(KeyError):
        md.preprocessors["rst-in-md"]


def test_load_extension_without_pymdownx(md):
    md = Markdown(
        extensions=[
            "rst_in_md",
            "attr_list",
            "fenced_code",
        ],
    )

    assert md.preprocessors.get_index_for_name("rst-in-md-configurator") == 0
    assert md.preprocessors["rst-in-md"]

    md.convert(source="placeholder")

    assert md.preprocessors["rst-in-md"]


def test_superfence_inside_admonition(md):
    plain = dedent("""
    ```rst
    +------------------------+------------+----------+----------+
    | Header row, column 1   | Header 2   | Header 3 | Header 4 |
    | (header rows optional) |            |          |          |
    +========================+============+==========+==========+
    | body row 1, column 1   | column 2   | column 3 | column 4 |
    +------------------------+------------+----------+----------+
    | body row 2             | Cells may span columns.          |
    +------------------------+------------+---------------------+
    | body row 3             | Cells may  | - Table cells       |
    +------------------------+ span rows. | - contain           |
    | body row 4             |            | - body elements.    |
    +------------------------+------------+---------------------+
    ```
    """).strip("\n")

    admonition = dedent("""
    !!! note
        ```rst
        +------------------------+------------+----------+----------+
        | Header row, column 1   | Header 2   | Header 3 | Header 4 |
        | (header rows optional) |            |          |          |
        +========================+============+==========+==========+
        | body row 1, column 1   | column 2   | column 3 | column 4 |
        +------------------------+------------+----------+----------+
        | body row 2             | Cells may span columns.          |
        +------------------------+------------+---------------------+
        | body row 3             | Cells may  | - Table cells       |
        +------------------------+ span rows. | - contain           |
        | body row 4             |            | - body elements.    |
        +------------------------+------------+---------------------+

        ```
    """).strip("\n")

    converted_plain = md.convert(source=plain)
    converted_admonition = md.convert(source=admonition)

    assert converted_plain in converted_admonition
