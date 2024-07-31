# rst-in-md

!!! warning
    This project is still in the early stages of development. Please be aware that there may be bugs, and the API may change. Please see the [limitations](./explanations/limitations.md) for more information.

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

<div class="md-typeset__scrollwrap">
   <div class="md-typeset__table">
      <table>
         <colgroup>
            <col width="43%">
            <col width="21%">
            <col width="18%">
            <col width="18%">
         </colgroup>
         <thead valign="bottom">
            <tr>
               <th>Header row, column 1\n(header rows optional)</th>
               <th>Header 2</th>
               <th>Header 3</th>
               <th>Header 4</th>
            </tr>
         </thead>
         <tbody valign="top">
            <tr>
               <td>body row 1, column 1</td>
               <td>column 2</td>
               <td>column 3</td>
               <td>column 4</td>
            </tr>
            <tr>
               <td>body row 2</td>
               <td colspan="3">Cells may span columns.</td>
            </tr>
            <tr>
               <td>body row 3</td>
               <td rowspan="2">Cells may\nspan rows.</td>
               <td colspan="2" rowspan="2">
                  <ul>
                     <li>Table cells
                     </li>
                     <li>
                        contain
                     </li>
                     <li>
                        body elements.
                     </li>
                  </ul>
               </td>
            </tr>
            <tr>
               <td>
                  body row 4
               </td>
            </tr>
         </tbody>
      </table>
   </div>
</div>


To get started, please head to [installation](./guides/installation.md) guide.

To understand how this tool works, you can read more about the [implementation](./explanations/implementation.md).
