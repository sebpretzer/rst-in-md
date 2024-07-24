import pytest
from bs4 import Tag

from rst_in_md import rst_to_soup


def test_fail():
    text = ".. table:: \n this is going to fail"
    with pytest.raises(ValueError, match="Failed to convert restructured text"):
        rst_to_soup(text)


def test_convert_multiple():
    text = """
.. table:: simple table
   :widths: auto

   =====  =====
     A    not A
   =====  =====
   False  True
   True   False
   =====  =====

.. list-table:: list table
   :widths: 15 10 30
   :header-rows: 1

   * - Treat
     - Quantity
     - Description
   * - Albatross
     - 2.99
     - On a stick!
   * - Crunchy Frog
     - 1.49
     - If we took the bones out, it wouldn't be
       crunchy, now would it?
   * - Gannet Ripple
     - 1.99
     - On a stick!
"""

    soup = rst_to_soup(text)

    tags = [t for t in soup.contents if isinstance(t, Tag)]
    assert len(tags) == 2

    table, list_table = tags

    assert table.name == "table"
    assert len(table.find_all("tr")) == 3
    assert len(table.find_all("caption")) == 1
    assert table.find_all("caption")[0].text == "simple table"

    assert list_table.name == "table"
    assert len(list_table.find_all("tr")) == 4
    assert len(list_table.find_all("caption")) == 1
    assert list_table.find_all("caption")[0].text == "list table"
