import re
import xlrd
from houseAttributes import House
from attributesConvert import *

file_location = "data.xlsx"
wb = xlrd.open_workbook(file_location)
sheet = wb.sheet_by_index(0)


def shapeConvert(i):
    switcher={
                'đa giác':1,
                'bình hành':2,
                'hình thang':3,
                'chữ nhật':4,
                'hình vuông':5,
             }
    return switcher.get(i, i)
# for index in range(4,sheet.nrows-1,+1):
#     print(shapeConvert(sheet.cell_value(index, 14).lower().strip()))


def directionConvert(i):
    switcher={
        'đông nam':1,
        'đông':2,
        'đông bắc':3,
        'bắc':4,
        'tây bắc':5,
        'tây':6,
        'tây nam':7,
        'nam':8
    }
    return switcher.get(i, i)

# for index in range(4,sheet.nrows-1,+1):
#     print(index)
#     print(directionConvert(sheet.cell_value(index, 15).lower().strip()))


def Characteristics(i):
    switcher={
                'nhà cấp 4 mái ngói':1,
                'nhà cấp 4':0.5,
                'mái lợp ngói':1.5,
                'mái ngói':1.5,
                'mái bê tông':2,
                'mái bằng bê tông':2,
                'bê tông cốt thép':3,
                'đang xây':2.5,
                'mái bằng bê tông cầu thang bê tông ban công':3,
                'mái bằng bê tông sân trước tường rào':2,
                'đất trống chưa có nhà':0,
                'x':0,
                '':0
             }
    return switcher.get(i, 1)
# for index in range(4,sheet.nrows-1,+1):
#     print(index)
#     print(Characteristics(sheet.cell_value(index, 37).lower().strip().replace(',', '').replace('.', '').replace('+', '')))

def limit(i):
    switcher={
        'x':0,
    }
    return switcher.get(i,i)

for index in range(4,sheet.nrows-1,+1):
    print(index)
    print(farFromConvert(sheet.cell_value(index, 39)))