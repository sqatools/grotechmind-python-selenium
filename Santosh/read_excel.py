import openpyxl

"""
pip install openpyxl

"""




def read_excel_file(filepath,row,col):
    wb_object=openpyxl.load_workbook(filepath)
    sheet_obj=wb_object.active
    cell_object=sheet_obj.cell(row=row,column=col)
    return cell_object.value


file_path = r"E:\excel\test2_data_xlsx.xlsx"
val = read_excel_file(file_path, 1, 1)
print(val)
