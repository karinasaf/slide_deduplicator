from difflib import SequenceMatcher


def similarity(a: str, b: str) -> float:
    """
    Return similarity ratio between two strings (0.0 to 1.0).
    """
    return SequenceMatcher(None, a, b).ratio()


def group_pages(pages_text: list[str], threshold: float) -> list[list[int]]:
    """
    Group consecutive pages that are similar.

    :param pages_text: list of extracted page texts
    :param threshold: similarity ratio to treat pages as same slide
    :return: list of groups of page indices
    """
    if not pages_text:
        return []

    groups = []
    current_group = [0]

    for i in range(1, len(pages_text)):
        prev_text = pages_text[i - 1]
        curr_text = pages_text[i]

        if similarity(prev_text, curr_text) >= threshold:
            current_group.append(i)
        else:
            groups.append(current_group)
            current_group = [i]

    groups.append(current_group)
    return groups
