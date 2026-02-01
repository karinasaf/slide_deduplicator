import argparse

from slide_deduplicator.reader import extract_pages_text
from  slide_deduplicator.grouper import group_pages
from  slide_deduplicator.selector import select_best_page
from  slide_deduplicator.writer import write_selected_pages


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Remove incomplete animation pages from a PDF."
    )
    parser.add_argument("input_pdf", help="Path to input PDF")
    parser.add_argument("output_pdf", help="Path to output PDF")
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.8,
        help="Similarity threshold for grouping pages (default: 0.8)",
    )

    args = parser.parse_args()

    pages_text = extract_pages_text(args.input_pdf)

    groups = group_pages(pages_text, args.threshold)

    selected_indices = [
        select_best_page(group, pages_text) for group in groups
    ]

    write_selected_pages(args.input_pdf, args.output_pdf, selected_indices)


if __name__ == "__main__":
    main()
