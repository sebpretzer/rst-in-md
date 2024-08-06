# Integrations

## MkDocs

To integrate with [MkDocs](https://www.mkdocs.org/), you simply need to make sure `rst-in-md` is [installed](./installation.md) and then add the following to your `mkdocs.yml` file:

```yaml
markdown_extensions:
  - attr_list
  - rst_in_md
```

## PyMdown Extensions SuperFences

The [SuperFences extension](https://facelessuser.github.io/pymdown-extensions/extensions/superfences/) overrides the default code block behavior in Python Markdown. To make sure `rst-in-md` is properly called, you simply need to specify the extension `pymdownx.superfences`:

```yaml hl_lines="4"
markdown_extensions:
  - attr_list
  - rst_in_md
  - pymdownx.superfences
```

You can read more about this integration in the [explanation](../explanations/implementation.md#integration-with-pymdown-extensions-superfences) and [reference](../reference/superfence.md#custom-fence).
