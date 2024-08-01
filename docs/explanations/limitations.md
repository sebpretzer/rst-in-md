# Limitations

## Unstable

The current implementation is unstable and may not work as expected. It has only been tested on a handful of test cases and may not work with all `reStructuredText` types.

To see the current tested types, please refer to the `tests/compatibility/rst/` directory.

## Loose Parity

There is no guarantee that the output of `rst-in-md` will produce identical html output as `Python-Markdown`. The goal is to produce as close a result as possible, so that downstream code any better format rst-based html, but there may be differences. Some of these differences are on purpose, to extend the functionality, while others are due to limitations in the current implementation. This will break something like the [class directive](https://docutils.sourceforge.io/docs/ref/rst/directives.html#class), which is stripped out.

## No support for `.rst` files

`rst-in-md` is designed to work with `reStructuredText` code blocks within `Markdown` files. It does not support `.rst` files directly. If you want to convert `.rst` files to `.md` files, you will need to use a different tool.
