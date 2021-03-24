import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split

xl = pd.ExcelFile('data.xlsx')
df = pd.read_excel(xl, 0, header=None)

x = ([])
y = []
for i in range(4, 490, +1):
    if df.at[i, 18] != 'x':
        x_data = [float(df.at[i, 11]), float(df.at[i, 12]), float(df.at[i, 13]), float(df.at[i, 18]), float(df.at[i, 20])]
        x.append(x_data)
        y.append(float(df.at[i, 20])*float(df.at[i, 13])*1000000)


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


X_train, X_test, Y_train, Y_test = train_test_split(np.nan_to_num(x), np.nan_to_num(y), test_size=0.2)
linearScore = linearRegressionModel(X_train, Y_train, X_test, Y_test)
print("Linear Score =" + str(linearScore))
lassoScore = lassoRegressionModel(X_train, Y_train, X_test, Y_test)
print("Lasso Score =" + str(lassoScore))

print(X_test)

