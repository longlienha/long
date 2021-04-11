import numpy as np
from numpy import reshape
from houseHelper import *
from attributesConvert import AtributesAndPrice
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from scipy.stats import linregress

file = "data.xlsx"
listHouse = getListHouse(file)
listAttributes = ([])
listPrice = []
AtributesAndPrice(listHouse,listAttributes,listPrice)
scaler = MinMaxScaler(feature_range=(0, 1))
rescaledAttributes = scaler.fit_transform(listAttributes)
# rescaledPrice = scaler.fit_transform(listPrice)
# rescaledPrice = rescaledPrice.reshape(-1,1)
X_train, X_test, Y_train, Y_test = train_test_split(np.float64(rescaledAttributes),np.float64(listPrice), test_size=0.2)
linearScore = linearRegressionModel(X_train, Y_train, X_test, Y_test)
lassoScore = lassoRegressionModel(X_train, Y_train, X_test, Y_test)
while linearScore < 0 or lassoScore < 0:
    X_train, X_test, Y_train, Y_test = train_test_split(np.float64(rescaledAttributes),np.float64(listPrice), test_size=0.2)
    linearScore = linearRegressionModel(X_train, Y_train, X_test, Y_test)
    lassoScore = lassoRegressionModel(X_train, Y_train, X_test, Y_test)

LR_Test_predict = LR_Test_predict(X_train, Y_train, X_test)
LR_MAPE = MAPE(Y_test,LR_Test_predict)
print("Linear Score =" + str(linearScore))
print("LR_MAPE",str(LR_MAPE))

LS_Test_predict  = LS_Test_predict(X_train, Y_train, X_test)
LS_MAPE = MAPE(Y_test,LS_Test_predict)
print("Lasso Score =" + str(lassoScore))
print("LS_MAPE",str(LS_MAPE))

# print(rescaledAttributes)
# print(Y_test)
# print(LS_Test_predict)
# front = []
# for attribute in listAttributes :
#     front.append(attribute[0])

# slope, intercept, rvalue, pvalue, stderr = linregress(listPrice, front)
# result = np.cov(listPrice,front)

# print(rvalue)
