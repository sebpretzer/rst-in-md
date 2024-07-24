# Inline Ignore

To use the inline ignore feature, add a comment right above the fenced code block:
```markdown
    <!-- ignore: rst-in-md -->
    ```rst
    With this comment, this will be ignored by the `rst-in-md` tool.
    ```

    ```rst
    This will be converted by the `rst-in-md` tool.
    ```
```

This will prevent the `rst-in-md` tool from converting the fenced code block directly following the comment. You will need to add a comment for each code block you want to ignore.

To read more about this, check out the [implementation](../explanations/implementation.md#inline-ignore) guide.
