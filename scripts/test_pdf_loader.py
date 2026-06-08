from backend.app.services.pdf_loader import load_pdf

PDF_PATH = "data/uploads/sample.pdf"

documents = load_pdf(PDF_PATH)

print(f"Pages Loaded: {len(documents)}")

print("\n")

print(documents[0].page_content[:1000])