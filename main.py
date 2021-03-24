from houseHelper import *
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split

file = "data.xlsx"
listHouse = getListHouse(file)
listAttributes = ([])
listPrice = []
for house in listHouse:
    houseAttributes = [house.front,house.dept,house.area,house.timeTranfer]
    listAttributes.append(houseAttributes)
    listPrice.append(float(house.priceTranfer)*float(house.area)*1000000)

X_train, X_test, Y_train, Y_test = train_test_split(listAttributes,listPrice, test_size=0.2)
linearScore = linearRegressionModel(X_train, Y_train, X_test, Y_test)
print("Linear Score =" + str(linearScore))
lassoScore = lassoRegressionModel(X_train, Y_train, X_test, Y_test)
print("Lasso Score =" + str(lassoScore))