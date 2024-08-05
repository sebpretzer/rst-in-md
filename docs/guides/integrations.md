# Integrations

## MkDocs

To integrate with [MkDocs](https://www.mkdocs.org/), you simply need to make sure `rst-in-md` is installed and then add the following to your `mkdocs.yml` file:

```yaml
markdown_extensions:
  - rst_in_md
```

## PyMdown Extensions SuperFences

[PyMdown Extensions SuperFences](https://facelessuser.github.io/pymdown-extensions/extensions/superfences/) override the default code block behavior in Python Markdown. To make sure `rst-in-md` is properly called, you need to specify the custom fence in your `mkdocs.yml` file:

```yaml
markdown_extensions:
  - pymdownx.superfences:
      custom_fences:
        - name: rst
          class: rst-in-md
          format: !!python/name:rst_in_md.superfence_formatter
          validator: !!python/name:rst_in_md.superfence_validator
        - name: rest
          class: rst-in-md
          format: !!python/name:rst_in_md.superfence_formatter
          validator: !!python/name:rst_in_md.superfence_validator
        - name: restructuredtext
          class: rst-in-md
          format: !!python/name:rst_in_md.superfence_formatter
          validator: !!python/name:rst_in_md.superfence_validator
```

You can find the reference for the extension [here](../reference/superfence.md).

!!! note
    You only need to specify the custom fence for the languages you are using in your code blocks (`rst`, `rest`, `rst-in-md`). For example, if all your code blocks are marked as `rst`, you only need to specify the custom fence for `rst`, and you can ignore the other two.
