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
