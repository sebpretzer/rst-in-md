# Integrations

## MkDocs

To integrate with [MkDocs](https://www.mkdocs.org/), you simply need to make sure `rst-in-md` is [installed](./installation.md) and then add the following to your `mkdocs.yml` file:

```yaml
markdown_extensions:
  - attr_list
  - rst_in_md
```

## PyMdown Extensions SuperFences

[PyMdown Extensions' SuperFences](https://facelessuser.github.io/pymdown-extensions/extensions/superfences/) override the default code block behavior in Python Markdown. To make sure `rst-in-md` is properly called, you simply need to specify the extension:

```yaml hl_lines="4"
markdown_extensions:
  - attr_list
  - rst_in_md
  - pymdownx.superfences
```

Usually, `pymdownx.superfences` require custom fences to be specified. However, `rst-in-md` automatically detects that `pymdownx.superfences` is installed and will properly handle the configuration for you.

You can find the reference for the extension [here](../reference/superfence.md#custom-fence).
