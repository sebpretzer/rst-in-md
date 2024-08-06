# Inline Ignore

To use the inline ignore feature, add an attribute to the code block you do not wish to convert like so: `#!markdown ```{.rst rst-in-md=false}`. This will prevent the `rst-in-md` tool from converting the fenced code block directly following the comment.

Bare in mind, _you will need to add a comment for each code block you want to ignore_. To understand why it was implemented this way, check out the [implementation](../explanations/implementation.md#inline-ignore) guide.



## Ignore conversion
How the ignore attribute works:
### Before
```markdown hl_lines="1" title="ignore.md"
    ```{.rst rst-in-md=false}
    With this comment, this will be ignored by the `rst-in-md` tool.
    ```
```
### After
```{.rst rst-in-md=false}
With this comment, this will be ignored by the `rst-in-md` tool.
```

## With conversion

### Before
```markdown title="normal.md"
    ```rst
    This will be converted by the `rst-in-md` tool.
    ```
```
### After
```rst
This will be converted by the `rst-in-md` tool.
```
