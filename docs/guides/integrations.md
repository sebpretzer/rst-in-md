# Integrations

## mkdocs

To integrate with [mkdocs](https://www.mkdocs.org/), you simply need to make sure `rst-in-md` is installed and then add the following to your `mkdocs.yml` file:

```yaml
markdown_extensions:
  - rst_in_md
```

## PyMdown Extensions SuperFences

[PyMdown Extensions SuperFences](https://facelessuser.github.io/pymdown-extensions/extensions/superfences/) override the default code block behavior in Python Markdown. To make sure `rst-in-md` is properly called, you need to specify the custom fence in your `mkdocs.yml` file:


```yaml
  - pymdownx.superfences:
      custom_fences:
        - name: [rst, rest, restructuredtext]
          format: !!python/name:rst_in_md.superfence
```
