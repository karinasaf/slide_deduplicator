def select_best_page(group: list[int], pages_text: list[str]) -> int:
    """
    Select the index of the 'best' page from a group.
    Currently defined as the page with the most text.
    """
    return max(group, key=lambda i: len(pages_text[i]))
