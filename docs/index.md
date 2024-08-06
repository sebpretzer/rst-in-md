# rst-in-md

`rst-in-md` is a simple tool to convert [reStructuredText](https://docutils.sourceforge.io/rst.html) within [Markdown](https://daringfireball.net/projects/markdown/), built to extend [Python Markdown](https://python-markdown.github.io/).


You can make full use of more complex `reStructuredText` elements, and they will be rendered correctly in the final output. Turn something like this:

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

Into this:
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


To get started, please head to [installation](./guides/installation.md) guide.

To understand how this tool works, you can read more about the [implementation](./explanations/implementation.md).
