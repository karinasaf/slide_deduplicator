from slide_deduplicator.grouper import group_pages


def test_groups_similar_pages():
    pages_text = [
        "Title\nSentence 1",
        "Title\nSentence 1\nSentence 2",
        "Next slide\nText",
        "Next slide\nText\nMore",
    ]

    groups = group_pages(pages_text, threshold=0.7)

    assert groups == [[0, 1], [2, 3]]


def test_single_page():
    pages_text = ["Only one slide"]

    groups = group_pages(pages_text, threshold=0.7)

    assert groups == [[0]]


def test_empty_input():
    pages_text = []

    groups = group_pages(pages_text, threshold=0.7)

    assert groups == []
