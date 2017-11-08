#All Subsets Regression - Generalized Linear Models
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt

def sp(arr, n):
    s = 0
    for k in range(n):
        s += arr[k][k]
    return s
def nullfinder(pop, n):
    val_ = True
    for o in range(n):
        for p in range(n):
            if pop[o][p] != 0:
                val_ = False
                break
    return val_
#faddev inverse matrix
def INVERSE_MATRIX(arr, n):
    E = np.matrix(np.identity(n))
    E = np.array(E)
    print_val = -10
    temp_arr = np.matrix(n, dtype=float)
    temp_arr = np.array(temp_arr)
    static_arr = arr
    Bn = arr
    for i in range(n):
        P = sp(arr, n) / (i + 1)
        if i == n - 1:
            print_val = Bn / P
        Bn = arr - (P * E)
        arr = np.matmul(static_arr, Bn)
        if nullfinder(arr, n):
            print("the end")
            break
    return print_val

def sumXY(arr1,arr2,n):
    sum_ = 0
    for i in range(n):
        sum_ += arr1[i]*arr2[i]
    return sum_

def sumX(arr, n):
    sum_ = 0
    for i in range(n):
        sum_ += arr[i]
    return sum_

def COMPUTE_REGRESSION_X(muffin, featureRows, featurSize, n): # featureRows =2 featureSize=5
    x = np.zeros(shape=(n, n))
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                x[i][i] = featureSize
            elif j == 0 and i >= 1:#
                x[i][j] = sumX(muffin[i - 1], featureSize)
            elif i == 0 and j >= 1:
                x[i][j] = sumX(muffin[j-1], featureSize)
            #elif i > 0 and j > 0:
            else:
                x[i][j] = sumXY(muffin[i-1], muffin[j-1], featureSize)
    return x

def COMPUTE_REGRESSION_Y_EX(yp, x1, x2, x3, n):  # stands for experimental
    y = np.zeros(4, dtype=float)
    for i in range(n):
        y[0] += yp[i]
        y[1] += yp[i] * x1[i]
        y[2] += yp[i] * x2[i]
        y[3] += yp[i] * x3[i]
    return y

def COMPUTE_REGRESSION_Y(yp,muffin, n, featureSize):
    y = np.zeros(n, dtype=float)
    for i in range(n):
        if i==0:
            y[i] = sumX(yp,featureSize)
        else:
            y[i] = sumXY(yp,muffin[i-1],featureSize)
    return y

df=pd.read_csv("Water Salinity and River Discharge.csv")
#plt.scatter(df)
#plt.show()
print(df.head())
#arr = np.zeros(shape=df['X1'].)
print(df["X1"].head())
X1=df['X1']
X2=df['X2']
X3=df['X3']
Y=df['Y']



featureSize = df.__len__()
featureRows = 3

print("featureSize = ",featureSize)

muffin = np.zeros(shape=(3, featureSize))
muffin[0]=X1
muffin[1]=X2
muffin[2]=X3

n=featureRows+1 #number of feature rows +1 for b0,b1,b2...
X=COMPUTE_REGRESSION_X(muffin,featureRows,featureSize,n)
vector1 = COMPUTE_REGRESSION_Y_EX(Y, muffin[0], muffin[1],muffin[2], featureSize)
vector = COMPUTE_REGRESSION_Y(Y, muffin,featureRows+1, featureSize)

print(X)
print(vector1)
print(vector)

inverse_arr = INVERSE_MATRIX(X, n)
print(inverse_arr)

B = np.matmul(inverse_arr, vector)
print()
print(B)

