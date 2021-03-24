from houseHelper import *
from attributesConvert import AtributesAndPrice
from sklearn.model_selection import train_test_split

file = "data.xlsx"
listHouse = getListHouse(file)
listAttributes = ([])
listPrice = []
AtributesAndPrice(listHouse,listAttributes,listPrice)
X_train, X_test, Y_train, Y_test = train_test_split(listAttributes,listPrice, test_size=0.2)
linearScore = linearRegressionModel(X_train, Y_train, X_test, Y_test)
print("Linear Score =" + str(linearScore))
lassoScore = lassoRegressionModel(X_train, Y_train, X_test, Y_test)
print("Lasso Score =" + str(lassoScore))