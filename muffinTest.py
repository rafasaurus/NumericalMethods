import numpy as np

def nullfinder(pop, n):
    val_ = True
    for o in range(n):
        for p in range(n):
            if pop[o][p] != 0:
                val_ = False
                break
    return val_

def sp(arr, n):
    s = 0
    for k in range(n):
        s += arr[k][k]
    return s


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

k=4
featureSize=4
muffin = np.zeros(shape=(k, featureSize))
muffin = [1,0,1,3,
          1,3,5,4,
          3,3,1,1,
          1,2,0,2]
muffin = np.reshape(muffin,(4,4))
print(muffin)

inverse = INVERSE_MATRIX(muffin,4)
print(inverse)

