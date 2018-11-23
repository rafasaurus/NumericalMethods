import numpy as np
x=0
y=0
f_1 = np.matrix([x,1,2,2])
f_1 = f_1.reshape(2,2)
f_1111 = np.matrix([0,0])
f_1111 = f_1111.reshape(2,1)
print(f_1111[1])

for i in range(20):

    f_delta = np.matrix([(1/(1-float(f_1111[0]))), float(f_1111[0])/(-1+float(f_1111[0])),
                         1/(2-2*float(f_1111[0])), 1/(-2+2*float(f_1111[0]))])
    f_delta = f_delta.reshape(2, 2)
    f = np.matrix([float(f_1111[1]) - float(f_1111[0])**2 - 5, float(f_1111[1]) - 2*float(f_1111[0])-4])
    f = f.reshape(2, 1)
    print(np.matmul(f_delta,f))
    f_1111 = f_1111 - np.matmul(f_delta,f)
