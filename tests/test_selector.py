from slide_deduplicator.selector import select_best_page


def test_selects_longest_text():
    pages_text = [
        "Short",
        "Short\nLonger",
        "Short\nLonger\nLongest",
    ]

    group = [0, 1, 2]

    best = select_best_page(group, pages_text)

    assert best == 2
