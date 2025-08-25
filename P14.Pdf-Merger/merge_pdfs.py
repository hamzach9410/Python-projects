from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(input_paths, output_path):
    # Creating a PdfWriter object
    merger = PdfWriter()
    
    # Adding each page of each PDF to the merger
    for path in input_paths:
        pdf = PdfReader(path)
        for page in range(len(pdf.pages)):
            merger.add_page(pdf.pages[page])
    
    # Writing the merged PDF to the output file
    with open(output_path, 'wb') as output_file:
        merger.write(output_file)
    print(f"Merged PDF saved as {output_path}")

def split_pdf(input_path, output_prefix, start_page, end_page):
    # Creating a PdfReader object
    pdf = PdfReader(input_path)
    
    # Creating a PdfWriter object for the split portion
    splitter = PdfWriter()
    for page in range(start_page - 1, end_page):
        splitter.add_page(pdf.pages[page])
    
    # Writing the split PDF to the output file
    output_path = f"{output_prefix}_pages_{start_page}-{end_page}.pdf"
    with open(output_path, 'wb') as output_file:
        splitter.write(output_file)
    print(f"Split PDF saved as {output_path}")

def add_watermark(input_path, watermark_path, output_path):
    # Creating PdfReader objects
    pdf = PdfReader(input_path)
    watermark = PdfReader(watermark_path)
    
    # Creating a PdfWriter object
    output = PdfWriter()
    
    # Adding watermark to each page
    for page_num in range(len(pdf.pages)):
        page = pdf.pages[page_num]
        page.merge_page(watermark.pages[0])  # Assuming watermark is on the first page
        output.add_page(page)
    
    # Writing the watermarked PDF to the output file
    with open(output_path, 'wb') as output_file:
        output.write(output_file)
    print(f"Watermarked PDF saved as {output_path}")

# Example usage with full file paths
if __name__ == "__main__":
    # Update these paths to match the location of your PDF files
    pdf_files = [
        "F:/python/projects/10.PdfMerger/document1.pdf",
        "F:/python/projects/10.PdfMerger/document2.pdf",
        "F:/python/projects/10.PdfMerger/document3.pdf"
    ]
    merge_pdfs(pdf_files, "F:/python/projects/10.PdfMerger/merged_output.pdf")

    # Split a PDF (e.g., pages 2 to 4)
    split_pdf("F:/python/projects/10.PdfMerger/merged_output.pdf", "split_output", 2, 4)

    # Add watermark (ensure you have a watermark PDF)
    add_watermark("F:/python/projects/10.PdfMerger/merged_output.pdf", 
                  "F:/python/projects/10.PdfMerger/watermark.pdf", 
                  "F:/python/projects/10.PdfMerger/watermarked_output.pdf")