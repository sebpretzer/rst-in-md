# ruff: noqa: E501
from textwrap import dedent

import pytest
from bs4 import BeautifulSoup

from rst_in_md import rst_to_soup


def test_simple_table():
    text = """
.. table::
   :widths: auto

   =====  =====  ======
      Inputs     Output
   ------------  ------
     A      B    A or B
   =====  =====  ======
   False  False  False
   True   False  True
   False  True   True
   True   True   True
   =====  =====  ======
    """
    rst_soup = rst_to_soup(dedent(text).strip("\n"))

    soup = BeautifulSoup(
        """
        <table>
        <thead valign="bottom">
            <tr><th colspan="2">Inputs</th><th>Output</th></tr>
            <tr><th>A</th><th>B</th><th>A or B</th></tr>
        </thead>
        <tbody valign="top">
            <tr><td>False</td><td>False</td><td>False</td></tr>
            <tr><td>True</td><td>False</td><td>True</td></tr>
            <tr><td>False</td><td>True</td><td>True</td></tr>
            <tr><td>True</td><td>True</td><td>True</td></tr>
        </tbody>
        </table>
        """,
        features="html.parser",
    )

    assert rst_soup.prettify() == soup.prettify()


def test_grid_table():
    text = """
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
    """
    rst_soup = rst_to_soup(dedent(text).strip("\n"))
    soup = BeautifulSoup(
        """
        <table>
            <colgroup><col width="43%"/><col width="21%"/><col width="18%"/><col width="18%"/></colgroup>
            <thead valign="bottom">
                <tr><th>Header row, column 1\n(header rows optional)</th><th>Header 2</th><th>Header 3</th><th>Header 4</th></tr>
            </thead>
            <tbody valign="top">
                <tr><td>body row 1, column 1</td><td>column 2</td><td>column 3</td><td>column 4</td></tr>
                <tr><td>body row 2</td><td colspan="3">Cells may span columns.</td></tr>
                <tr><td>body row 3</td><td rowspan="2">Cells may\nspan rows.</td><td colspan="2" rowspan="2"><ul><li>Table cells</li><li>contain</li><li>body elements.</li></ul></td></tr>
                <tr><td>body row 4</td></tr>
            </tbody>
        </table>
        """,
        features="html.parser",
    )

    assert rst_soup.prettify() == soup.prettify()


@pytest.fixture()
def list_table_factory():
    def _list_table_factory(title: str = "", widths: str = "auto") -> str:
        # https://docutils.sourceforge.io/docs/ref/rst/directives.html#list-table
        text = f"""
.. list-table:: {title}
  :widths: {widths}
  :header-rows: 1

  * - Treat
    - Quantity
    - Description
  * - Albatross
    - 2.99
    - On a stick!
  * - Crunchy Frog
    - 1.49
    - If we took the bones out, it wouldn't be crunchy, now would it?
  * - Gannet Ripple
    - 1.99
    - On a stick!
        """
        return dedent(text).strip("\n")

    return _list_table_factory


def test_auto_widths_table(list_table_factory):
    rst_soup = rst_to_soup(list_table_factory(widths="auto"))

    soup = BeautifulSoup(
        """
        <table>
        <thead valign="bottom">
            <tr><th>Treat</th><th>Quantity</th><th>Description</th></tr>
        </thead>
        <tbody valign="top">
            <tr><td>Albatross</td><td>2.99</td><td>On a stick!</td></tr>
            <tr><td>Crunchy Frog</td><td>1.49</td><td>If we took the bones out, it wouldn't be crunchy, now would it?</td></tr>
            <tr><td>Gannet Ripple</td><td>1.99</td><td>On a stick!</td></tr>
        </tbody>
        </table>
        """,
        features="html.parser",
    )

    assert rst_soup.prettify() == soup.prettify()


def test_fixed_widths_table(list_table_factory):
    rst_soup = rst_to_soup(list_table_factory(widths="15 10 30"))

    soup = BeautifulSoup(
        """
        <table>
        <colgroup><col width="27%"/><col width="18%"/><col width="55%"/></colgroup>
        <thead valign="bottom">
            <tr><th>Treat</th><th>Quantity</th><th>Description</th></tr>
        </thead>
        <tbody valign="top">
            <tr><td>Albatross</td><td>2.99</td><td>On a stick!</td></tr>
            <tr><td>Crunchy Frog</td><td>1.49</td><td>If we took the bones out, it wouldn't be crunchy, now would it?</td></tr>
            <tr><td>Gannet Ripple</td><td>1.99</td><td>On a stick!</td></tr>
        </tbody>
        </table>
        """,
        features="html.parser",
    )

    assert rst_soup.prettify() == soup.prettify()
