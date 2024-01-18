import openpyxl

def read_excel_data(file_name,row,col):
    wb_obj=openpyxl.load_workbook(file_path)
    sheet_obj=wb_obj.active
    cell_obj=sheet_obj.cell(row=row,column=col)
    return cell_obj.value

file_path=r"D:\Python_Automation\Test_data.xlsx"
val=read_excel_data(file_path,1,1)
print(val)


