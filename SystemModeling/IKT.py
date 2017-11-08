import numpy as np

arr = np.zeros(shape=(19,19))
zeros=arr
x = np.array([1, 1, 2, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 16, 17, 18, 19], np.float)
y = np.array([8, 11, 13, 12, 16, 5, 14, 6, 15, 7, 19, 9, 0, 9, 19, 7, 16, 18, 14, 17, 0, 0, 0, 0], np.float)
x_temp=9
y_temp=0
for i in range(19):
    for j in range(19):
        for k in range(19):
            arr[int(x[k])-1][int(y[k]-1)]=1


print()
print(arr)

print()

#arr_2=np.matmul(arr,arr)
#print(arr_2)
global_arr=arr
while global_arr.any() != zeros.any():
    global_arr =np.matmul(global_arr,global_arr)
    print(global_arr)