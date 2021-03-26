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
        oneHouse.shape = shapeConvert(sheet.cell_value(index, 14))
        oneHouse.direction = directionConvert(sheet.cell_value(index, 15))
        oneHouse.Characteristics = Characteristics(sheet.cell_value(index, 37))
        oneHouse.limit = limit(sheet.cell_value(index, 25))
        oneHouse.roadHouse = sheet.cell_value(index, 22)
        oneHouse.landPosition = sheet.cell_value(index, 21)
        oneHouse.serviceQuanlity = serviceQuanlity(sheet.cell_value(index, 47))
        oneHouse.placesToNear = placesToNear(sheet.cell_value(index, 45))
        oneHouse.farFromCity = sheet.cell_value(index, 39)
        oneHouse.farFromDistrict = sheet.cell_value(index, 40)
        oneHouse.farFromPark = sheet.cell_value(index, 42)
        oneHouse.typeOfHouse = typeOfHouse(sheet.cell_value(index, 29))
        oneHouse.houseEntryCharacteristics = serviceQuanlity(sheet.cell_value(index, 48))
        oneHouse.houseNumber = HouseNumber(sheet.cell_value(index, 52))
        oneHouse.sanitaryCondition = SanitaryCondition(sheet.cell_value(index, 50))
        oneHouse.floors = floors(sheet.cell_value(index, 51))
        oneHouse.rooms = rooms(sheet.cell_value(index, 31))
        oneHouse.levelOfHouse = levelOfHouse(sheet.cell_value(index, 30))
        oneHouse.currentLandValue = currentLandValue(sheet.cell_value(index, 17))
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
