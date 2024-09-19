import PyPDF2


def merge_pdfs(pdf_list, output_filename):
    pdf_merger = PyPDF2.PdfMerger()

    # Loop through all the PDFs
    for pdf in pdf_list:
        with open(pdf, "rb") as file:
            pdf_merger.append(file)

    # Write the merged PDF to an output file
    with open(output_filename, "wb") as output_file:
        pdf_merger.write(output_file)


# Example usage:
pdfs_to_merge = ["Deloitte.pdf", "Grade.pdf"]  # Replace with your PDF file names
output_pdf = "Deloitte1.pdf"  # The name of the merged PDF

merge_pdfs(pdfs_to_merge, output_pdf)
