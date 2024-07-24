from rst_in_md import RestructuredTextInMarkdownPreProcessor


def test_load_extension(md):
    converted = md.convert(source=(source := ""))
    assert source == converted

    assert any(
        isinstance(p, RestructuredTextInMarkdownPreProcessor) for p in md.preprocessors
    )


def test_higher_priority_than_html_block(md):
    rst_index = md.preprocessors.get_index_for_name("rst-in-md")
    html_index = md.preprocessors.get_index_for_name("html_block")
    assert rst_index < html_index


def test_higher_priority_than_fenced_code(md):
    rst_index = md.preprocessors.get_index_for_name("rst-in-md")
    fenced_code_index = md.preprocessors.get_index_for_name("fenced_code_block")
    assert rst_index < fenced_code_index
