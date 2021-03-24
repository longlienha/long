import xlrd
from houseAttributes import House
from sklearn import linear_model
from sklearn.model_selection import train_test_split

# file_location = "data.xlsx"
# wb = xlrd.open_workbook(file_location)
# sheet = wb.sheet_by_index(0)
# print (type(sheet.cell_value(4, 11)))
# print(sheet.nrows)
# listHouse = []
# for index in range(4,sheet.nrows-1,+1):
#     oneHouse = House()
#     oneHouse.front = sheet.cell_value(index, 11)
#     oneHouse.dept = sheet.cell_value(index,12)
#     oneHouse.area = sheet.cell_value(index,13)
#     oneHouse.timeTranfer = sheet.cell_value(index,18)
#     oneHouse.priceTranfer = sheet.cell_value(index,20)
#     listHouse.append(oneHouse)

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