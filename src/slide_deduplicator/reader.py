from pypdf import PdfReader


def extract_pages_text(path: str) -> list[str]:
    """
    Extract text from each page of a PDF.

    :param path: Path to input PDF file
    :return: List of page texts in order
    """
    reader = PdfReader(path)

    pages_text = []
    for page in reader.pages:
        text = page.extract_text()
        pages_text.append(text if text else "")

    return pages_text
