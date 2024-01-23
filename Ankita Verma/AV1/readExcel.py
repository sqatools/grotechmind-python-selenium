import openpyxl


def read_excel(filepath, row, col):
    re_obj = openpyxl.load_workbook(filepath)
    sheet_read = re_obj.active
    cell_obj = sheet_read.cell(row=row, column=col)
    return cell_obj.value


filepath = r"C:\GitPrograms\grotechmind-python-selenium\Ankita Verma\AV1\read_python.xlsx"
#filepath= "read_python.xlsx"
# val1 = read_excel(filepath, ,6)#?????
# print(val1)



for i in range(1,6):
    val1 = read_excel(filepath, i, 1)
    print(val1)
