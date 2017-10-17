import numpy as np
n = 4
# the matrix

arr = np.array([1, 2, 3, 2,
                0, 4, 1, 1,
                3, 5, 6, 0,
                2, 0, 3, 4], np.float32)
arr = arr.reshape(n, n)
y = np.zeros(shape=(n))
y[0] = 1
y[1] = 3
y[2] = 1
y[3] = 0
# size of the matrix
def GausJordan(arr,y,n):
    for j in range (n):
        flag = True
        for i in range(n):
            if i!=j:
                if arr[j][j]!=0:
                    const=arr[i][j]/arr[j][j];
                    for k in range(n):
                        arr[i][k]=arr[i][k]-const*arr[j][k];
                        if flag:
                            flag = False
                            y[i] = y[i] - const * y[i]
    return arr,y

arr,y=GausJordan(arr,y,n)
print("new\n",arr)
print("new y \n",y)

#the answer calc
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

