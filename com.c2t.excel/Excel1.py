# Reading an excel file using Python
import xlrd

# Give the location of the file
loc = ("path of file")

# To open Workbook
wb = xlrd.open_workbook('Excel_Sample.xlsx')
sheet = wb.sheet_by_index(0)

# For row 0 and column 0
print('sheet.cell_value(0, 0)=',sheet.cell_value(0, 0))

print('sheet.nrows=',sheet.nrows)
print('sheet.ncols=',sheet.ncols)

for colCount in range(sheet.ncols):
    print(sheet.cell_value(0, colCount))

for rowCount in range(sheet.nrows):
    print(sheet.cell_value(rowCount,0))