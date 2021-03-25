def AtributesAndPrice(listHouse,listAttributes,listPrice):
    for house in listHouse:
        houseAttributes = [house.front,house.dept,house.area,house.timeTranfer]
        listAttributes.append(houseAttributes)
        listPrice.append(float(house.priceTranfer)*float(house.area)*1000000)

def yearConvert(year):
    if year == 'x':
        year = float(1)
    if year == '':
        year = float(1)
    return year

def areaConvert(area = float):
    if area == '':
        area = float(1)
    return area

def deptConvert(dept = float):
    if dept == '':
        dept = float(1)
    return dept

def frontConvert(front = float):
    if front == '':
        front = float(1)
    return front

def shapeConvert(i):
    i.lower().strip()
    switcher={
                'đa giác':1,
                'bình hành':2,
                'hình thang':3,
                'chữ nhật':4,
                'hình vuông':5,
             }
    return switcher.get(i, i)

def directionConvert(i):
    i.lower().strip()
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

def Characteristics(i):
    i.lower().strip().replace(',', '').replace('.', '').replace('+', '')
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

def limit(i):
    i.lower().strip()
    switcher={
        'x':1,
    }
    return switcher.get(i,0)

def serviceQuanlity(i):
    i.lower().strip()
    switcher={
        'tốt':1,
        'trung bình':2
    }
    return switcher.get(i,0)

def placesToNear(i):
    i.lower().strip()
    switcher={
        'trung tâm tp':1,
        'người thân':2,
        'chỗ làm việc':3,
        'trường học':4,
        'công viên':5,
        'siêu thị':6
    }
    return switcher.get(i,0)
