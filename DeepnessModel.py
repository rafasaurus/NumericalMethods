# finite difference model
#def computeDiffDepth():# computes optimal depth of model
import numpy as np
def mean(arr,n):
    s=0
    for i in range(n):
        s+=arr[i]
    return s/n
def standardDevation(z,featureSize,deepness):
    z_mean=mean(z,featureSize)
    sum = 0
    for i in range(deepness,featureSize):
        sum+=z[i]-z_mean
    return sum/(featureSize-3*deepness)
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
#Computes C matrix using finite difference model
def computeC(x,z,featureSize,deepness):
    out = np.zeros(shape=(deepness*2,deepness*2))
    vector = np.zeros(shape=(deepness * 2))

    for o in range(deepness*2):
        vectorEven = np.zeros(shape=(deepness))
        vectorOdd = np.zeros(shape=(deepness))
        for l in range(0, deepness):#j
            #print()
            for k in range(deepness - 1, featureSize):#i
                if o%2 == 0:
                    index = k - (int)(o / 2)
                    #print(index)
                    vectorEven[l] +=  x[k - l]*x[index]
                    vectorOdd[l] += z[k - l]*x[index]
                else:
                    index = k - (int)(o / 2)
                    vectorEven[l - 1] += x[k - l]*z[index]
                    vectorOdd[l - 1] += z[k - l]*z[index]
        #print("vector Even \n ", vectorEven)
        #print("vector Odd \n ", vectorOdd)
        # this part adds Even and Odd vectors
        for i in range(deepness * 2):
            if i % 2 == 0:
                index = (int)(i / 2)
                vector[i] = vectorEven[index]
            else:
                index = (int)((i / 2))
                vector[i] = vectorOdd[index]
        #print(vector)
        out[o] = vector
    return out
#calculates finite differnce model constant vector
def computeD(x,z,featureSize,deepness):
    vector = np.zeros(shape=(deepness * 2))
    for l in range(0, deepness*2):  # j
        for k in range(deepness - 1, featureSize):  # i
           vector[l]+=z[k]*x[k-l]
    return vector

deepness = 1
featureSize = 7
x = np.array([2, 4, 1, 3, 1, 2, 4], np.float)
z = np.array([2, 1, 1, 2, 2, 3, 4], np.float)
z_hat = np.zeros(shape=(4, featureSize))

previousStandardDev =1
while(1):
    print("-------iteration------")
    C = computeC(x, z, featureSize, deepness)
    print("C = \n",C)
    C_inverse = INVERSE_MATRIX(C, deepness * 2)
    print("C_inverse = \n",C_inverse)
    D = computeD(x, z, featureSize, deepness)
    print("D= \n", D)
    ANSWER = np.matmul(C_inverse, D)
    print(ANSWER)
    standardDev = standardDevation(z, featureSize, deepness)
    print("standard deviation",standardDev)
    if (standardDev<=previousStandardDev or deepness == 1):
        deepness+=1
    else:
        print()
        print("----------conclusion-----------")
        print("the deepness of the given model with finite difference model is --->",deepness)
        print("the standard deviation in that deepness is --->",standardDev)
        break
    previousStandardDev = standardDev
