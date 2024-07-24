# Installation

## From PyPI

Install `rst-in-md` using [PyPI](https://pypi.org/project/rst-in-md/):

```bash
pip install rst-in-md
```
or
```bash
uv add rst-in-md
```

## From Source

If you want to manually install it, run:

```bash
uv run hatchling build
```
and then install the wheel file generated in the `dist/` directory.


## Locally

If you want to use it locally, you can clone the repository and run:

```bash
uv add . --editable
```

Now you can [use the extension](./general_usage.md) in your markdown files.
