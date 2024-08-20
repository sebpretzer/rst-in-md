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

!!! warning "Auto-Configuration"
    By installing both `rst-in-md` and `pymdownx.superfences`, you invoke an [auto-configurator](../reference/superfence.md#rst_in_md.RestructuredTextInMarkdownAutoConfigurator) that will remove `rst-in-md` and add the proper custom fences for `pymdownx.superfences`. It is equivalent to the following configuration:

    ```diff
    markdown_extensions:
      - attr_list
    - - rst_in_md
      - pymdownx.superfences:
    +     custom_fences:
    +       - name: rst
    +         class: rst-in-md
    +         format: !!python/name:rst_in_md.superfence_formatter
    +        validate: !!python/name:rst_in_md.superfence_validator
    +       - name: rest
    +         class: rst-in-md
    +         format: !!python/name:rst_in_md.superfence_formatter
    +         validate: !!python/name:rst_in_md.superfence_validator
    +       - name: restructuredtext
    +         class: rst-in-md
    +         format: !!python/name:rst_in_md.superfence_formatter
    +         validate: !!python/name:rst_in_md.superfence_validator
    ```

    If you want to customize the `custom_fences`, you can do so by simply not including `rst-in-md` in the `markdown_extensions` and specifying the `custom_fences` yourself.

    _The auto-configurator will work with [other custom fences like `mermaid.js`](https://facelessuser.github.io/pymdown-extensions/extras/mermaid/#using-in-mkdocs) as well, so only do this if you want to customize the `rst-in-md` superfences in particular._
