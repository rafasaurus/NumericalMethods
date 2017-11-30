import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
'''
df = pd.read_csv("Water Salinity and River Discharge.csv")
regr = LinearRegression()

df_numpy = df.as_matrix()
print(df.head(5))
print(df_numpy[:,4])
Y = df_numpy[:,4]
X1 = df_numpy[:,1]
X2 = df_numpy[:,2]
X3 = df_numpy[:,3]
Y = Y.reshape(1,-1)
X1 = X1.reshape(1,-1)
X2 = X2.reshape(1,-1)
X3 = X3.reshape(1,-1)

regr.fit(X1,Y)
#lm.fit(X1,Y)
m = regr.coef_[0]
b=regr.intercept_
print("m= ",m)
print("b= ",b )

plt.scatter(X1, Y,  color='green')
#plt.scatter(X2, Y,  color='blue')

#plt.scatter(X3, Y,  color=


#plt.plot(X1,Y_, color='blue',linewidth = 1)




plt.show()
'''


# your input arrays
#x = [[a, 26] for a in range(1, 70, 1)]
#y = [192770, 14817993,1393537, 437541, 514014, 412468, 509393, 172715, 329806, 425876, 404031, 524371, 362817, 692020, 585431, 446286, 744061, 458805, 330027, 495654, 459060, 734793, 701697, 663319, 750496, 525311,1045502, 250641, 500360, 507594, 456444, 478666, 431382, 495689, 458200, 349161, 538770, 355879, 535924, 549858, 611428, 517146, 239513, 354071, 342354, 698360, 467248, 500903, 625170, 404462,1057368, 564703, 700988,1352634, 727453, 782708, 1023673,1046348,1175588, 698072, 605187, 684739, 884551,1067267, 728643, 790098, 580151, 340890, 299185]
df = pd.read_csv("Water Salinity and River Discharge.csv")

x1 = df['X1'].values[:,np.newaxis]
x2 = df['X2'].values[:,np.newaxis]
x3 = df['X3'].values[:,np.newaxis]
featureSize=len(x1)
featureCols = 2
x_ = np.zeros(shape=(0,featureSize))
x_ = np.append(x_,x1)
x_ = np.append(x_,x2)
#np.concatenate((x_, x1))

# target data is array of shape (n,)
y = df['Y'].values
x_ = x_.reshape(featureSize,-featureCols) #reshaping for .fit method
print(x_)
## your code for regression
regr = LinearRegression()
regr.fit(x_, y)

# the correct coef is different from your findings
print (regr.coef_)
print (regr.intercept_)
