# You will need to install the 'PyPDF2' library: pip install PyPDF2
import PyPDF2

def read_pdf_file(file_path):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfFileReader(file)
        content = ""

        for i in range(reader.getNumPages()):
            page = reader.getPage(i)
            content += page.extractText()

    return content

file_path = "example.pdf"
content = read_pdf_file(file_path)
print(content)
