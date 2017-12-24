import numpy as np

np.set_printoptions(threshold=1000)

arr = np.zeros(shape=(19,19),dtype=int)
compareZeroMatrix = np.zeros(shape=(19,19),dtype=int)
zeros=arr
#x = np.array([1, 1, 2, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 16, 17, 18, 19], np.float)
x = np.array([1, 1,  2,  2,  3,  3, 4,  4, 5,  6, 7,  8, 9, 10,11,12, 13, 14, 15, 16,16,17,18,19], np.int)
y = np.array([8, 11, 13, 12, 16, 5, 14, 6, 15, 7, 19, 9, 0, 9, 19, 7, 16, 18, 14, 17, 0, 0, 0, 0], np.int)# 24 elements
x_temp=9
y_temp=0

for i in range(19):
    for j in range(19):
        for k in range(24):
            if y[k]-1 !=0 and y[k]!=0:
                #if ((int(y[k]-1)==19 and int(x[k])-1)==19):
                arr[int(x[k])-1][int(y[k]-1)]=1


#first matrix A^1
print(arr)
print()

global_arr = np.zeros(shape=(19,19),dtype=int)
global_arr = arr.copy()
matrix_sum = np.zeros(shape=(19,19),dtype=int)
N = 0
while(np.array_equal(global_arr,compareZeroMatrix)==False):
    matrix_sum += global_arr
    global_arr=np.matmul(global_arr,arr)
    N += 1
    print("n=", N)
    print("boolean check = ", np.array_equal(global_arr,compareZeroMatrix))
    print(global_arr )


    #print(global_arr)

print("N=",N)
print("-----հասանելիության մատրից-----")
print(matrix_sum)
#print("debug=",global_arr)
#global_arr=arr
#while global_arr.any() != zeros.any():
#    global_arr =np.matmul(global_arr,global_arr)
#    print(global_arr)

#if all([v==0 for v in arr]):
#    global_arr =np.matmul(global_arr,global_arr)
#    print(global_arr)