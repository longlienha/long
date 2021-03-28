
import math
from numpy import float64


def AtributesAndPrice(listHouse,listAttributes,listPrice):
    for house in listHouse:
        # houseAttributes = [house.front,house.dept,math.ceil(house.area),house.timeTranfer,house.shape,house.direction,house.Characteristics,
        # house.limit,house.landPosition,house.toiletQuality,house.placesToNear,house.farFromPark,house.farFromCulture,
        # house.typeOfHouse,house.houseEntryCharacteristics,house.houseNumber,house.floors,house.rooms,house.totalFloorArea,house.totalArea,house.timeOfLandUse,house.buildingPermit,
        # house.whenGetBP,house.buildTime,house.schoolQuality,house.streetCharacteristics,house.store,house.typeStore,house.diagram,house.roadHouse,
        # house.farFromCity,house.farFromDistrict,house.farFromSchool,house.levelOfHouse,house.timeOfLandUse,house.currentPropertyValue]
        houseAttributes = house.attributes()
        listAttributes.append(houseAttributes)
        housePrice = [float(house.priceTranfer)*float(house.area)*1000000,house.currentLandValue]
        listPrice.append(housePrice)

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
    switcher={
                'đa giác':1.0,
                'bình hành':2.0,
                'hình thang':3.0,
                'chữ nhật':4.0,
                'hình vuông':5.0,
                'chữ l':2.0
             }
    return switcher.get(i, 0)

def directionConvert(i):
    switcher={
        'đông nam':1.0,
        'đông':2.0,
        'đông bắc':3.0,
        'bắc':4.0,
        'tây bắc':5.0,
        'tây':6.0,
        'tây nam':7.0,
        'nam':8.0
    }
    return switcher.get(i, 0)

def Characteristics(i):
    switcher={
                'nhà cấp 4 mái ngói':1.0,
                'nhà cấp 4':0.5,
                'mái lợp ngói':1.5,
                'mái ngói':1.5,
                'mái bê tông':2.0,
                'mái bằng bê tông':2.0,
                'bê tông cốt thép':3.0,
                'đang xây':2.5,
                'mái bằng bê tông cầu thang bê tông ban công':3.0,
                'mái bằng bê tông sân trước tường rào':2.0,
                'đất trống chưa có nhà':0.0,
                'x':0.0,
                '':0.0
             }
    return switcher.get(i, 1.0)

def limit(i):
    switcher={
        'x':1.0,
    }
    return switcher.get(i,0.0)
def roadHouse(i):
    switcher={
        '4 met': 4.0
    }
    result = switcher.get(i,i)
    if type(result) == str:
        return 0.0
    return float(result)

def serviceQuality(i):
    switcher={
        'tốt':2.0,
        'tốt':2.0,
        'trung bình':1.0,
        '':0
    }
    return switcher.get(i,0.0)

def placesToNear(i):
    switcher={
        'trung tâm tp':1.0,
        'người thân':2.0,
        'chỗ làm việc':3.0,
        'trường học':4.0,
        'công viên':5.0,
        'siêu thị':6.0
    }
    return switcher.get(i,0.0)

def typeOfHouse(i):
    switcher={
        'nhà tập thể':1.0,
        'bán kiên cố':2.0,
        'kiên cố':3.0
    }
    return switcher.get(i,0.0)

def HouseEntryCharacteristics(i):
    switcher={
        'khó vào':1.0,
        'thuận tiện cho xe máy':2.0,
        'thuận tiện cho ô tô':3.0
    }
    return switcher.get(i,0.0)

def SanitaryCondition(i):
    switcher={
        'kém':1.0,
        'trung bình':2.0,
        'tốt':3.0,
    }
    return switcher.get(i,0.0)

def HouseNumber(i):
    switcher={
        'có':1.0,
        'chưa':2.0
    }
    return switcher.get(i,0.0)

def floors(i):
    switcher={
        'x':0.0
    }
    result = switcher.get(i,i)
    if type(result) == str:
        return 0.0
    return float(result)

def rooms(i):
    switcher={
        'x':0.0,
        'đang xây':0.0,
        '':0.0
    }
    result = switcher.get(i,i)
    if type(result) == str:
        return 0.0
    return float(result)

def levelOfHouse(i):
    switcher={
        'x':float64(0)
    }
    result = switcher.get(i,i)
    if type(result) == str:
        return 0.0
    return float(result)


def currentLandValue(i):
    switcher={
        'x':float64(0),
        '':float64(0),
        'Không có':float64(0)
    }
    result = switcher.get(i,i)
    if type(result) == str:
        return float(0)
    return float64(result)*1000000

def diagram(i):
    switcher={
        'có':1.0,
        'không':2.0
    }
    return switcher.get(i,0.0)

def totalFloorArea(i):
    switcher={
        'x':0.0,
        '':0.0
    }
    result = switcher.get(i,i)
    if type(result) == str:
        return 0.0
    return float(result)

def timeOfLandUse(i):
    switcher={
        'lâu dài':1,
    }
    return switcher.get(i,0.0)

def floatConvert(i):
    switcher={
        'x':0.0,
        '':0.0
    }
    string = switcher.get(i,i)
    if type(string) == str:
        return 0.0
    else:
        return string

def streetCharacteristics(i):
    switcher={
        'phố dân cư':1.0,
        'phố kinh doanh':2.0,
        '':0.0
    }
    result = switcher.get(i,i)
    if type(result) == str:
        return 0.0
    return float(result)

def store(i):
    switcher={
        'x':1.0,
        'có':2.0
    }
    return switcher.get(i,0.0)

def typeStore(i):
    switcher={
        'tạp phẩm':1.0,
        'may mặc':2.0,
        'dịch vụ photo':3.0,
        'thợ mộc':4.0,
        'linh kiện đồ điện tử':5.0,
        'y tế':6.0
    }
    return switcher.get(i,0.0)

def farFromConvert(i):
    if type(i) == str:
        return 0.0
    else: 
        return float(i)