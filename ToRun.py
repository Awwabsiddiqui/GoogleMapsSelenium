import openpyxl

from main import mainMethod

wb_obj = openpyxl.load_workbook("input/input.xlsx")

sheet_obj = wb_obj.active
m_row = sheet_obj.max_row

for i in range(2, m_row + 1):
        cell_obj = sheet_obj.cell(row=i, column=1)
        print(cell_obj.value)
        mainMethod(cell_obj.value , 3 , 10)