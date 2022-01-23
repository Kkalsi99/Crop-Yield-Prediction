import combineData
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import TruncatedSVD
from sklearn.svm import SVC

df = combineData.Dataset()
# print(df.columns)
df = df[["Rainfall", "Area","Production"]]
df = df.fillna(0)

X_train = df[["Rainfall","Area"]]

# print(X)
Y_train = df["Production"]
# print(Y_train)
print(X_train)
X_train, X_test, y_train, y_test = train_test_split(X_train, Y_train, test_size=0.3, random_state=43, shuffle=True)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

clf = LinearRegression().fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(mean_squared_error(y_test, y_pred, squared=False))
print(mean_absolute_error(y_test, y_pred))
print(r2_score(y_test, y_pred))


from sklearn.ensemble import RandomForestRegressor

clf = RandomForestRegressor()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
# print(y_pred)
# print(y_test)
print("rfr")

print(mean_squared_error(y_test, y_pred, squared=False))


print(mean_absolute_error(y_test, y_pred))
print(r2_score(y_test, y_pred))
num = []
for i in range(X_test.shape[0]):
    num.append(i + 1)

plt.scatter(num, y_pred, label="Predicted")

# plt.ylim(0, 10)
# plt.xlim(0, 100)
plt.legend()
plt.xlabel("Datapoints")
plt.ylabel("Production")
plt.show()
plt.scatter(num, y_test, label="Actual")
# plt.ylim(0, 10)
# plt.xlim(0, 100)
plt.legend()
plt.xlabel("Datapoints")
plt.ylabel("Production")
plt.show()

print("gbr")
from sklearn.ensemble import GradientBoostingRegressor

reg = GradientBoostingRegressor(random_state=0).fit(X_train, y_train)
y_pred = reg.predict(X_test)
print(mean_squared_error(y_test, y_pred, squared=False))
print(mean_absolute_error(y_test, y_pred))
print(r2_score(y_test, y_pred))
print("svr")
from sklearn.svm import SVR
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

regr = make_pipeline(StandardScaler(), SVR(C=1.0, epsilon=0.2))
regr.fit(X_train, y_train)
y_pred = regr.predict(X_test)
print(mean_squared_error(y_test, y_pred, squared=False))

print(mean_absolute_error(y_test, y_pred))
print(r2_score(y_test, y_pred))
