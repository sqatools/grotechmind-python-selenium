import openpyxl
"""
pip install openpyxl
"""

def read_excel_file(filepath, row, col):
    wb_object = openpyxl.load_workbook(filepath)
    sheet_obj = wb_object.active
    cell_object = sheet_obj.cell(row=row, column=col)
    return cell_object.value

file_path = r"D:\Python\GitRepo\grotechmind-python-selenium\Nagarjuna\PythonFile Handling\Test_Data.xlsx"
val = read_excel_file(file_path, 1, 1)
print(val)

print("@"*20)
for i in range(1, 4):
    val = read_excel_file(file_path, i, 1)
    print(val)

print("%"*30)
