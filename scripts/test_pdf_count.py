from pathlib import Path

pdf_files = list(
    Path("data/uploads").rglob("*.pdf")
)

print(
    f"PDF Count: {len(pdf_files)}"
)