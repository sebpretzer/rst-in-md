# Motivation

The goal of Markdown is to provide an easy-to-read, easy-to-write plain text format that can be converted into HTML. It is designed to be as simple as possible, while still providing a rich set of features. [Python-Markdown](https://python-markdown.github.io/) provides an excellent implementation of the [Markdown spec](https://daringfireball.net/projects/markdown/syntax), and it has near parity.

But the issue is that the Markdown specification is not as rich as it could be. There are many features that are not supported, and [many tools](https://github.com/Python-Markdown/markdown/wiki/Third-Party-Extensions) have extended the functionality where they see fit, chief among them being [pymdown-extensions](https://facelessuser.github.io/pymdown-extensions/). The goal of `rst-in-md` is to further extend that goal, and provide an even richer set of features, where current functionality is lacking.

[reStructuredText](https://docutils.sourceforge.io/rst.html) has a similar philosophy to Markdown, as it attempts to be easy-to-read, albeit less easy-to-write. It is extremely popular in the python community, meaning it is relatively robust and dependable. And there should be a lot of examples for users to draw from. Providing a way to embed `reStructuredText` in Markdown, and have it render as expected, can provide a lot of value to users.
