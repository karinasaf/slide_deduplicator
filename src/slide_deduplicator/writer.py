from pypdf import PdfReader, PdfWriter


def write_selected_pages(input_pdf: str, output_pdf: str, indices: list[int]) -> None:
    """
    Write selected pages (by index) from input_pdf into output_pdf.

    :param input_pdf: path to source PDF
    :param output_pdf: path to destination PDF
    :param indices: list of page indices to keep
    """
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for i in indices:
        writer.add_page(reader.pages[i])

    with open(output_pdf, "wb") as f:
        writer.write(f)
