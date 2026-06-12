from pathlib import Path

pdf_files = Path(
    "data/uploads"
).rglob("*.pdf")

for pdf_file in pdf_files:

    print(
        pdf_file.name,
        "->",
        pdf_file.parent.name
    )

    break