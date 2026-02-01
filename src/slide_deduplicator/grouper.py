from difflib import SequenceMatcher


def similarity(a: str, b: str) -> float:
    """
    Compute a similarity ratio between two strings.

    :param a: First string
    :param b: Second string
    :return: Float between 0.0 and 1.0 indicating similarity
    """
    return SequenceMatcher(None, a, b).ratio()


def group_pages(pages_text: list[str], threshold: float) -> list[list[int]]:
    """
    Group consecutive pages that belong to the same slide based on text similarity.

    Pages are grouped by comparing each page to the first page of the current group.
    This prevents chaining errors where unrelated slides are grouped together.

    :param pages_text: List of extracted text for each page
    :param threshold: Similarity threshold above which pages are grouped
    :return: List of groups, each a list of page indices
    """
    if not pages_text:
        return []

    groups = []
    current_group = [0]

    for i in range(1, len(pages_text)):
        first_index = current_group[0]

        if similarity(pages_text[first_index], pages_text[i]) >= threshold:
            current_group.append(i)
        else:
            groups.append(current_group)
            current_group = [i]

    groups.append(current_group)
    return groups
