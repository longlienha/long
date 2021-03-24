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