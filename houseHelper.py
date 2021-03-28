import xlrd
from houseAttributes import House
from attributesConvert import *
from sklearn import linear_model
from sklearn.model_selection import train_test_split

def getListHouse(file):
    # file_location = "data.xlsx"
    wb = xlrd.open_workbook(file)
    sheet = wb.sheet_by_index(0)
    listHouse = []
    for index in range(4,sheet.nrows-1,+1):
        oneHouse = House()
        oneHouse.front = frontConvert(sheet.cell_value(index, 11))
        oneHouse.dept = deptConvert(sheet.cell_value(index,12))
        oneHouse.area = float(areaConvert(sheet.cell_value(index,13)))
        oneHouse.timeTranfer = yearConvert(sheet.cell_value(index,18))
        oneHouse.priceTranfer = sheet.cell_value(index,20)
        oneHouse.shape = shapeConvert(sheet.cell_value(index, 14).lower().strip())
        oneHouse.direction = directionConvert(sheet.cell_value(index, 15).lower().strip())
        oneHouse.Characteristics = Characteristics(sheet.cell_value(index, 37).lower().strip().replace(',', '').replace('.', '').replace('+', ''))
        oneHouse.limit = limit(sheet.cell_value(index, 25).lower().strip())
        oneHouse.roadHouse = roadHouse(sheet.cell_value(index, 22))
        oneHouse.landPosition = sheet.cell_value(index, 21)
        oneHouse.toiletQuality = serviceQuality(sheet.cell_value(index, 50).lower().strip())
        oneHouse.placesToNear = placesToNear(sheet.cell_value(index, 45).lower().strip())
        oneHouse.farFromCity = farFromConvert(sheet.cell_value(index, 39))
        oneHouse.farFromDistrict = farFromConvert(sheet.cell_value(index, 40))
        oneHouse.farFromPark = farFromConvert(sheet.cell_value(index, 42))
        oneHouse.farFromCulture = farFromConvert(sheet.cell_value(index, 41))
        oneHouse.farFromSchool = farFromConvert(sheet.cell_value(index, 44))
        oneHouse.farFromMarket = farFromConvert(sheet.cell_value(index, 43))
        oneHouse.typeOfHouse = typeOfHouse(sheet.cell_value(index, 29).lower().strip())
        oneHouse.houseEntryCharacteristics = serviceQuality(sheet.cell_value(index, 48).lower().strip())
        oneHouse.houseNumber = HouseNumber(sheet.cell_value(index, 52).lower().strip())
        oneHouse.sanitaryCondition = SanitaryCondition(sheet.cell_value(index, 50).lower().strip())
        oneHouse.floors = floors(sheet.cell_value(index, 51))
        oneHouse.rooms = rooms(sheet.cell_value(index, 31))
        oneHouse.levelOfHouse = levelOfHouse(sheet.cell_value(index, 30))
        oneHouse.currentLandValue = currentLandValue(sheet.cell_value(index, 17))
        oneHouse.currentPropertyValue = currentLandValue(sheet.cell_value(index, 16))
        oneHouse.valueOfTransferredRealOstate = currentLandValue(sheet.cell_value(index, 19))
        oneHouse.diagram = diagram(sheet.cell_value(index, 26).lower().strip())
        oneHouse.totalFloorArea = rooms(sheet.cell_value(index, 31))
        oneHouse.totalArea = rooms(sheet.cell_value(index, 32))
        oneHouse.timeOfLandUse = timeOfLandUse(sheet.cell_value(index, 27).lower().strip())
        oneHouse.buildingPermit = floatConvert(sheet.cell_value(index, 34))
        oneHouse.whenGetBP = floatConvert(sheet.cell_value(index, 35))
        oneHouse.buildTime = floatConvert(sheet.cell_value(index, 33))
        oneHouse.schoolQuality = serviceQuality(sheet.cell_value(index, 46).lower().strip())
        oneHouse.medicalQuality = serviceQuality(sheet.cell_value(index, 47).lower().strip())
        oneHouse.streetCharacteristics = streetCharacteristics(sheet.cell_value(index, 49).lower().strip())
        oneHouse.store = store(sheet.cell_value(index, 54).lower().strip())
        oneHouse.typeStore = typeStore(sheet.cell_value(index, 55).lower().strip())
        listHouse.append(oneHouse)

    return listHouse

def linearRegressionModel(X_train, Y_train, X_test, Y_test):
    linear = linear_model.LinearRegression()
    # Training process
    linear.fit(X_train, Y_train)
    # Evaluating the model
    score_trained = linear.score(X_test, Y_test)
    return score_trained

def lassoRegressionModel(X_train, Y_train, X_test, Y_test):
    lasso_linear = linear_model.Lasso(alpha=1.0)
    # Training process
    lasso_linear.fit(X_train, Y_train)
    # Evaluating the model
    score_trained = lasso_linear.score(X_test, Y_test)
    return score_trained
