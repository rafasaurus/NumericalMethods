#!/usr/bin/env python
# -*- coding: utf-8 -*-
#All Subsets Regression - Generalized Linear Models
import numpy as np
import pandas as pd
import itertools

F_TABLE = 0.35


def findsubsets(S,m):
    return set(itertools.combinations(S, m))

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

#Faddeev inverse matrix
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

def COMPUTE_Y(yp,muffin, n, featureSize):
    y = np.zeros(n, dtype=float)
    for i in range(n):
        if i==0:
            y[i] = sumX(yp,featureSize)
        else:
            y[i] = sumXY(yp,muffin[i-1],featureSize)
    return y

def mean(arr,n):
    s=0
    for i in range(n):
        s+=arr[i]
    return s/n

#ռեգրեսիայով պայմանավորված միջին քառակուսային շեղումներ
def SSR(arr,featureSize):
    arr_mean = mean(arr, featureSize)
    SSR_ = 0
    for i in range(n):
        SSR_ += (arr[i] - arr_mean) * (arr[i] - arr_mean)
    return SSR_

#միջին քառակուսային շեղումներ
def SS0(arr,featureSize):
    SS0_ = 0
    arr_mean = mean(arr, featureSize)
    for i in range(featureSize):
        SS0_ += (arr[i] - arr_mean) * (arr[i] - arr_mean)
    return SS0_

#դետերմինացման գործակից
def RSquared(arr,featureSize):
    return SSR(arr,featureSize)/SS0(arr,featureSize)

#ռեգռեսիայով պայմանավորված դիսպերսիան
def MSR(arr,featureSize,dof):
    MSR_ = SSR(arr,featureSize)/(dof)# featureRows+1 is "degrees of freedom"
    return MSR_

#անհամաձայնեցումներով պայմանավորված միջին քառակուսային շեղումներ
def SSE(yp,y_final,featureSize):
    SSE_ = 0
    for i in range(featureSize):
        SSE_+=(y_final[i] - yp[i])*(y_final[i] - yp[i])
    return SSE_

#մնացորդային դիսպերսիայի վիճակագրական գնահատական, ազատության աստիճանը n-k-1
def sigmaSquared(yp,y_final,feautreSize,dof):
    sigmaSquared_ = SSE(yp,y_final,featureSize)/(featureSize-dof-1)
    return sigmaSquared_

#ֆիշերի չափանիշ
def FISHER(yp,y_final,featureSize,dof):
    F = MSR(y_final,featureSize,dof)/(sigmaSquared(yp,y_final,featureSize,dof))
    return F
def fact(n):
    fact_=1
    for i in range(1,n+1):
        fact_=fact_*i
    return fact_

def combinatorial(n,k):
    return fact(n) / (fact(n - k) * fact(k))

def getB_index(featureRows,df,global_iter):

    S = [1, 2, 3]
    S=findsubsets(S, global_iter)
    return S


def computeN(N,df,Fisher_bool):#computes regression for N variables
    featureSize = df.__len__()
    featureRows = 3
    X1 = df['X1']
    X2 = df['X2']
    X3 = df['X3']
    Y = df['Y']
    X_ = np.zeros(shape=(3, featureSize))
    X_[0] = X1
    X_[1] = X2
    X_[2] = X3

    global_iter = featureRows
    dof = featureRows  # var that has been used for comuting SSR,SSE... for degrees of freedom

    maxes_index = 0
    maxes = np.zeros(shape=(global_iter))

    while global_iter != 0 and Fisher_bool==1:


        c=combinatorial(featureRows,global_iter)
        #print("c=",c)

        B_indexes=getB_index(featureRows, df, global_iter)
        print("B_indexes=",B_indexes)


        list_=[]

        for index in B_indexes:
            for index_of_index in index:

                    #print(index_of_index)
                    list_.append(index_of_index)

            print("  ")
        #print(list_)
        print("--------end----------")

        middle_muffin = np.zeros(shape=(global_iter, featureSize))
        #print("middle_muff",middle_muffin)
        reg_i_step = 0

        experimental_reg=0

        r_squared_bool=True
        for c_i in range(int(c)):#0
            for regression_i in range(global_iter):
                if global_iter==featureRows:
                    middle_muffin[regression_i] = X_[list_[regression_i]-1]
                else:
                    middle_muffin[regression_i] = X_[list_[reg_i_step] - 1]
                    reg_i_step+=1

            n = global_iter + 1
            #n = featureRows + 1  # number of feature rows +1 for b0,b1,b2...
            X = COMPUTE_REGRESSION_X(middle_muffin, global_iter, featureSize, n)
            vector = COMPUTE_Y(Y, middle_muffin, global_iter +1, featureSize)

            inverse_arr = INVERSE_MATRIX(X, n)

            B = np.matmul(inverse_arr, vector)
            append_ = np.zeros(shape=(featureRows+1-B.__len__()))
            B = np.append(B,append_)
            # print()
            print("B=",B)

            each_reg=list_.__len__()/c
            y_final = np.zeros(shape=(featureSize))

            for each_reg_i in range(each_reg):
                print("list_exp = ",list_[experimental_reg])
                for i in range(featureSize):
                    for c_i_i in range(1,featureRows):
                        if c_i_i==0:
                            y_final[i] = y_final+B[0]
                        y_final[i] = y_final[i] + B[list_[c_i_i]] * X_[list_[experimental_reg]-1][i]
                experimental_reg = experimental_reg + 1
            print(y_final)

            if (r_squared_bool):
                r_squared_bool=False
                max=RSquared(y_final,featureSize)

            if (RSquared(y_final,featureSize)>max):
                max=RSquared(y_final,featureSize)
            print("r_squared= ", RSquared(y_final,featureSize))

        global_iter = global_iter - 1
        print("max=",max)
        maxes[maxes_index]=max
        maxes_index = maxes_index+1
        dof_Fisher = featureSize - featureRows - 1
        for q in range(featureRows-1):
            FISHER=((pow(maxes[q],2)-pow(maxes[q+1],2))/dof_Fisher)/(1-pow(maxes[q],2))
            print("FISHER","i=",featureRows-q,"j=",featureRows-q-1,FISHER)
            if (FISHER>F_TABLE):
                print("")
                print("the best subset regression is ", "i=", featureRows - q, "j=", featureRows - q - 1, FISHER)
                Fisher_bool = 0
                break
    print("maxes=",maxes)



#---------------------------------------program--------------------------------------------------------
df=pd.read_csv("Water Salinity and River Discharge.csv")

X1=df['X1']
X2=df['X2']
X3=df['X3']
Y=df['Y']

featureSize = df.__len__()
featureRows = 3

dof = featureRows # var that has been used for comuting SSR,SSE... for degrees of freedom

muffin = np.zeros(shape=(3, featureSize))
muffin[0]=X1
muffin[1]=X2
muffin[2]=X3

n=featureRows+1 #number of feature rows +1 for b0,b1,b2...
X=COMPUTE_REGRESSION_X(muffin,featureRows,featureSize,n)

N=4#regression for N variables
Fisher_bool = 1
computeN(N,df,Fisher_bool)

print("-----------------------")
global_iter=featureRows
getB_index(featureRows,df,global_iter)

