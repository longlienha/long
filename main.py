import numpy as np
from houseHelper import *
from attributesConvert import AtributesAndPrice
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

file = "data.xlsx"
listHouse = getListHouse(file)
listAttributes = ([])
listPrice = ([])
AtributesAndPrice(listHouse,listAttributes,listPrice)
X_train, X_test, Y_train, Y_test = train_test_split(np.float64(listAttributes),np.float64(listPrice), test_size=0.2)
linearScore = linearRegressionModel(X_train, Y_train, X_test, Y_test)
LR_Test_predict = LR_Test_predict(X_train, Y_train, X_test)
LR_MAPE = MAPE(Y_test,LR_Test_predict)
print("Linear Score =" + str(linearScore))
print("LR_MAPE",str(LR_MAPE))
lassoScore = lassoRegressionModel(X_train, Y_train, X_test, Y_test)
LS_Test_predict  = LS_Test_predict(X_train, Y_train, X_test)
LS_MAPE = MAPE(Y_test,LS_Test_predict)
print("Lasso Score =" + str(lassoScore))
print("LS_MAPE",str(LS_MAPE))
