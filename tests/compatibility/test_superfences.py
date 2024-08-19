import sys
from textwrap import dedent
from unittest.mock import patch

import pytest
from markdown import Markdown
from pymdownx.superfences import SuperFencesCodeExtension

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
    )


def test_no_auto_configurator_without_pymdownx():
    # https://stackoverflow.com/a/65034142
    with patch.dict(sys.modules, {k: None for k in sys.modules if "pymdownx" in k}):
        md = Markdown(
            extensions=[
                "rst_in_md",
                "attr_list",
                "fenced_code",
            ],
        )
        assert "rst-in-md-auto-configurator" not in md.preprocessors


def test_load_extension_with_pymdownx(md):
    assert md.preprocessors.get_index_for_name("rst-in-md-auto-configurator") == 0
    assert md.preprocessors["rst-in-md"]

    assert md.preprocessors["fenced_code_block"].config.get("custom_fences", []) == []

    md.convert(source="placeholder")

    with pytest.raises(KeyError):
        md.preprocessors["rst-in-md"]

    configs = md.preprocessors["fenced_code_block"].config.get("custom_fences", [])
    languages = ["rst", "rest", "restructuredtext"]
    assert len(configs) == len(languages)
    for config in configs:
        assert config["name"] in languages
        assert config["class"] == "rst-in-md"
        assert config["format"] == superfence_formatter
        assert config["validator"] == superfence_validator

    ext = None
    for _ext in md.registeredExtensions:
        if isinstance(_ext, SuperFencesCodeExtension):
            ext = _ext
            break

    assert ext is not None
    assert len(ext.superfences) == 4  # rst, rest, restructuredtext, built-in
    for fence in ext.superfences:
        if fence.get("name") == "superfences":
            continue
        assert fence.get("name") in languages


def test_load_extension_without_pymdownx(md):
    md = Markdown(
        extensions=[
            "rst_in_md",
            "attr_list",
            "fenced_code",
        ],
    )

    assert md.preprocessors.get_index_for_name("rst-in-md-auto-configurator") == 0
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
