def select_best_page(group: list[int], pages_text: list[str]) -> int:
    """
    Select the most complete page from a group of animation-step pages.

    Selection rules:
    - Prefer pages that contain extracted text over pages with no text.
    - Prefer pages with more text over pages with less text.
    - If multiple pages have the same amount of text, prefer the later page
      (assumed to be the final animation state).

    :param group: List of page indices belonging to the same slide
    :param pages_text: List of extracted text for all pages
    :return: Index of the selected page
    """
    non_empty = [i for i in group if pages_text[i].strip()]

    candidates = non_empty if non_empty else group

    return max(candidates, key=lambda i: (len(pages_text[i]), i))
