import numpy as np

def gauss(arr,n):
    print(arr)
    print(y)
    print()
    # matrix pivotisation
    for i in range(1, n):
        for j in range(i + 1, n):
            if arr[i][i] < arr[j][i]:
                q = np.zeros(shape=(4))
                q = q.reshape(1, n)
                q = arr[i]
                arr[i] = arr[j]
                arr[j] = q

                temp = y[i - 1]
                y[i - 1] = y[i]
                y[i] = temp
    print("after pivot")
    print(arr)
    print(y)
    # loop performs the gauss elimination
    for i in range(0, n - 1):
        flag = True
        for j in range(i + 1, n):
            for k in range(0, n):
                const = arr[i][k] / arr[i][i]
                arr[j][k] = arr[j][k] - arr[j][i] * const
                if flag:
                    y[i] = y[i] - const * y[i]
                    flag = False
    print("y vector after elimination = ", y)
    print("matrix after pivotation")
    print(arr)
    return arr
    #end of gaus() function

#def jordan(arr,n):
#    for i in range(0, n - 1):
#        flag = True
#        for j in range(i + 1, n):
#            for k in range(0, n):
#                const = arr[i][k] / arr[i][i]
#                arr[j][k] = arr[j][k] - arr[j][i] * const
#                if flag:
#                    y[i] = y[i] - const * y[i]
#                    flag = False

# the matrix
n = 4
arr = np.array([1, 2, 3, 2,
                0, 4, 1, 1,
                3, 5, 6, 0,
                2, 0, 3, 4], np.int32)
arr = arr.reshape(n, n)
# size of the matrix

# y is the right side of the linear equation after = sign
y = np.zeros(shape=(n))
y[0]=1
y[1]=3
y[2]=1
y[3]=0
arr = gauss(arr,n)
#arr =jordan(arr,n)


# x is the unknown vector
#this part calculates x unkown vector
x = np.array([0, 0, 0, 0], np.float16)
x = x.reshape(n, 1)
for i in range(n-1, -1, -1):
    x[i] = y[i]
    for j in range(i+1, n):
        if j != i:
            x[i] = x[i]-arr[i][j]*x[j]
    x[i] /= arr[i][i]
# prints x
print("x1=", x[0])
print("x2=", x[1])
print("x3=", x[2])
print("x4=", x[3])

