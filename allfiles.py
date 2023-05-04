# You will need to install the 'openpyxl' library: pip install openpyxl
import openpyxl

def read_excel_file(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    data = []

    for row in sheet.iter_rows(values_only=True):
        data.append(row)

    return data

file_path = "example.xlsx"
content = read_excel_file(file_path)
print(content)
