import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
from io import BytesIO

def merge_pdfs(pdf_files):
    pdf_writer = PdfWriter()
    
    for pdf_file in pdf_files:
        pdf_reader = PdfReader(pdf_file)
        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])
    
    merged_pdf = BytesIO()
    pdf_writer.write(merged_pdf)
    merged_pdf.seek(0)
    return merged_pdf

st.title("PDF Merger")

st.write("Lade mehrere PDF-Dateien hoch, um sie zu einer einzigen PDF-Datei zusammenzuführen.")

uploaded_files = st.file_uploader("Wähle PDF-Dateien aus", type="pdf", accept_multiple_files=True)

if uploaded_files:
    if st.button("PDFs zusammenführen"):
        merged_pdf = merge_pdfs(uploaded_files)
        st.success("PDFs erfolgreich zusammengeführt!")
        st.download_button(
            label="Heruntergeladene zusammengeführte PDF",
            data=merged_pdf,
            file_name="merged.pdf",
            mime="application/pdf"
        )
