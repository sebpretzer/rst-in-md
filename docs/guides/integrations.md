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

You can read more about this integration in the [explanation](../explanations/implementation.md#integration-with-pymdown-extensions-superfences) and [reference](../reference/superfence.md#superfence).

### Customizing Fences

By default, if `pymdownx.superfences` is installed, `rst-in-md` will automatically configure the custom fences for you via the [auto-configurator](../reference/superfence.md#rst_in_md.RestructuredTextInMarkdownAutoConfigurator). The auto-configurator will add the custom fences to the `pymdownx.superfences` configuration:

```yaml hl_lines="5-17"
markdown_extensions:
  - attr_list
  - rst_in_md
  - pymdownx.superfences:
      custom_fences:
        - name: rst
          class: rst-in-md
          format: !!python/name:rst_in_md.superfence_formatter
          validate: !!python/name:rst_in_md.superfence_validator
        - name: rest
          class: rst-in-md
          format: !!python/name:rst_in_md.superfence_formatter
          validate: !!python/name:rst_in_md.superfence_validator
        - name: restructuredtext
          class: rst-in-md
          format: !!python/name:rst_in_md.superfence_formatter
          validate: !!python/name:rst_in_md.superfence_validator
```

So, if the above configuration is not desired, you can simply turn off the auto-configurator by setting `auto_config` to `False`:

```yaml hl_lines="4"
markdown_extensions:
  - attr_list
  - rst_in_md:
      auto_config: False
  - pymdownx.superfences:
      custom_fences:
        - name: rest
          class: rst-in-md
          format: !!python/name:rst_in_md.superfence_formatter
          validate: !!python/name:rst_in_md.superfence_validator
```

Now, only `rest` fenced code blocks will be converted to reStructuredText.
