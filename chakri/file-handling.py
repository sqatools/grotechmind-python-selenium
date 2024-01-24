import openpyxl
filepath = r'C:\New folder (2)'
def filehandle(filepath,row,column):
    a = openpyxl.load_workbook(filepath)
    b = a.active
    c = b.cell(row=1,column=1)
    print(c)


filehandle(r'C:\New folder (2)',row=1,column=1)
