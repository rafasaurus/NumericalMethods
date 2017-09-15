import numpy as np

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


#def COMPUTE_REGRESSION_X(x1, x2, n):
#    arr = np.zeros(shape=(3, 3))
#    arr[0][0] = n
#    for i in range(n):
#        arr[0][1] += x1[i]
#        arr[0][2] += x2[i]
#        arr[1][1] += np.power(x1[i], 2)
#        arr[1][2] += x2[i] * x1[i]
#        arr[2][2] += np.power(x2[i], 2)
#    arr[1][0] = arr[0][1]
#    arr[2][1] = arr[1][2]
#    arr[2][0] = arr[0][2]
#    return arr

def COMPUTE_REGRESSION_X(muffin, featureRows, featurSize, n): # featureRows =2 featureSize=5
    x = np.zeros(shape=(n, n))
    print("----------------")
    print(type(x))
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
                debug = muffin[j]
                x[i][j] = sumXY(muffin[i-1], muffin[j-1], featureSize)
            #elif i > 1:

    return x

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


def COMPUTE_REGRESSION_Y_EX(yp, x1, x2, n):  # stands for experimental
    y = np.zeros(3, dtype=float)
    for i in range(n):
        y[0] += yp[i]
        y[1] += yp[i] * x1[i]
        y[2] += yp[i] * x2[i]
    return y


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
            print("debug")
        Bn = arr - (P * E)
        arr = np.matmul(static_arr, Bn)
        if nullfinder(arr, n):
            print("the e  nd")
            break
    return print_val

#
#-------program-------
n = 4
k = 2 #the number of regression features
k += 1

featureSize = 5
featureRows = 2

muffin = np.zeros(shape=(k, featureSize))
print("muffin=", muffin)
arr = np.zeros(shape=(4, 4))
muffin[0] = np.array([2, 1, 1, 2, 1], np.float)
muffin[1] = np.array([3, 1, 2, 1, 2], np.float)
yp = np.array([1, 1, 3, 2, 1], np.float)
arr = COMPUTE_REGRESSION_X(muffin, featureRows, featureSize, k)
print(arr)
vector = COMPUTE_REGRESSION_Y_EX(yp, muffin[0], muffin[1], 5)
print("arr=", arr)
inverse_arr = INVERSE_MATRIX(arr, 3)
print("vector=\n", vector)
B = np.matmul(inverse_arr, vector)
print(B)