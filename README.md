---

# Slide Deduplicator

Remove incomplete animation pages from PDFs exported from PowerPoint.

When PowerPoint slides with animations are exported to PDF using “one page per animation”, each animation step becomes a separate page.
This tool keeps only the final (complete) version of each slide.

---

## How it works

1. Extracts text from each PDF page.
2. Compares consecutive pages for similarity.
3. Groups pages that belong to the same slide.
4. Keeps the page with the most text from each group.
5. Writes a new PDF containing only complete slides.

It does **not** read PowerPoint animations.
It infers slide completeness from text similarity and length.

---

## Installation

Clone the repository and install in editable mode:

```bash
pip install -e .
```

If using Conda:

```bash
conda env create -f environment.yml
conda activate slide-deduplicator
```

---

## Usage

```bash
slide-deduplicator input.pdf output.pdf
```

Or:

```bash
python -m slide_deduplicator.main input.pdf output.pdf
```

Optional threshold (controls how similar pages must be to be grouped):

```bash
slide-deduplicator input.pdf output.pdf --threshold 0.8
```

Lower threshold → more aggressive grouping
Higher threshold → stricter grouping

---

## Project structure

```
src/slide_deduplicator/
├── reader.py    # extract text from PDF
├── grouper.py   # group similar pages
├── selector.py  # choose best page per group
├── writer.py    # write output PDF
└── main.py      # command-line interface
```

---

## Limitations

* Does not work on image-only PDFs (no extractable text).
* Assumes each animation step adds more text.
* May fail if different slides have very similar text.
* Cannot recover animation logic from the PDF.

---

## Testing

Run unit tests with:

```bash
pytest
```

---
