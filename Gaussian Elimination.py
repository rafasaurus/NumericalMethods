import numpy as np
# the matrix
arr = np.array([1, 2, 3, 2,
                0, 4, 1, 1,
                3, 5, 6, 0,
                2, 0, 3, 4], np.int32)
# size of the matrix
n = 4
# y is the right side of the linear equation after = sign
y = np.array([1, 3, 2, 1], np.float16)
y = y.reshape(n, 1)
arr = arr.reshape(n, n)
print(arr)
print()
# matrix pivotisation
for i in range(0, n):
    for j in range(i+1, n):
        if arr[i][i] < arr[j][i]:
            q = np.zeros(shape=(4))
            q = q.reshape(1, n)
            q[0] = arr[i]
            arr[i] = arr[j]
            arr[j] = q
            q = y[j]


# loop performs the gauss elimination

for i in range(0, n-1):
    for j in range(i+1, n):
        for k in range(0, n):
            arr[j][k] = arr[j][k]-arr[j][i]/arr[i][i]*arr[i][k]

print("matrix after pivotation")
print(arr)
# x is the unknown vector
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
