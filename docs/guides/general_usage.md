# General Usage

After [installing](./installation.md) the package, any [fenced code block](https://python-markdown.github.io/extensions/fenced_code_blocks/) with the language `rst` will be converted to `reStructuredText` by the `rst-in-md` tool.

## Basic Example

For example, this markdown:
```markdown
    ```rst
    .. table:: Truth table for "not"
       :widths: auto

       =====  =====
           A    not A
       =====  =====
       False  True
       True   False
       =====  =====
    ```
```

Will be converted to this `reStructuredText`:
```rst
.. table:: Truth table for "not"
   :widths: auto

   =====  =====
     A    not A
   =====  =====
   False  True
   True   False
   =====  =====
```

!!! note
    This will work for any [short names](https://pygments.org/docs/lexers/#pygments.lexers.markup.RstLexer) that are used for the `reStructuredText` language identifier:

    * `rst`
    * `restructuredtext`
    * `rest`

You can also [ignore specific code blocks](./inline_ignore.md) if you want them rendered the normal way.

## Supported Features

`reStructuredText` is a powerful markup language that can be used to create a lot of complex structures. This includes [directives like tables, images, etc](https://docutils.sourceforge.io/docs/ref/rst/directives.html). This also includes some [latex math support](https://docutils.sourceforge.io/docs/ref/rst/mathematics.html), which can be used to render equations.

The `rst-in-md` tool officially supports just a small subset of the features that `reStructuredText` provides, since a lot of them are redundant when used within a Markdown document.

Below are some of the features that are supported.

### Simple Tables

```markdown
    ```rst
    =====  =====
    A      B
    =====  =====
    False  False
    True   False
    False  True
    True   True
    =====  =====
    ```
```

```rst
=====  =====
A      B
=====  =====
False  False
True   False
False  True
True   True
=====  =====
```

### Grid Tables

```markdown
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
```

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

### List Tables

```markdown
    ```rst
    .. list-table:: Title
       :widths: 25 25 50
       :header-rows: 1

       * - Heading row 1, column 1
         - Heading row 1, column 2
         - Heading row 1, column 3
       * - Row 1, column 1
         -
         - Row 1, column 3
       * - Row 2, column 1
         - Row 2, column 2
         - Row 2, column 3
    ```
```

```rst
.. list-table:: Title
   :widths: 25 25 50
   :header-rows: 1

   * - Heading row 1, column 1
     - Heading row 1, column 2
     - Heading row 1, column 3
   * - Row 1, column 1
     -
     - Row 1, column 3
   * - Row 2, column 1
     - Row 2, column 2
     - Row 2, column 3
```

### Latex math support

```markdown
    ```rst
    .. math::

       \int_{-\infty}^\infty e^{-x^2} dx = \sqrt{\pi}
    ```
```

```rst
.. math::

   \int_{-\infty}^\infty e^{-x^2} dx = \sqrt{\pi}
```
