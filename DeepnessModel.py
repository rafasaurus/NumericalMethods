import numpy as np

def computeC(x,z,featureSize,deepness):
    out = np.zeros(shape=(deepness*2,deepness*2))
    print("out = ",out)
    print("debuug   ", out[0])
    vector = np.zeros(shape=(deepness * 2))

      # i

    for o in range(deepness*2):
        vectorEven = np.zeros(shape=(deepness))
        vectorOdd = np.zeros(shape=(deepness))
        for l in range(0, deepness):#j
            print()
            for k in range(deepness - 1, featureSize):#i
                if o%2 == 0:
                    index = k - (int)(o / 2)
                    print(index)
                    vectorEven[l] +=  x[k - l]*x[index]
                    vectorOdd[l] += z[k - l]*x[index]
                else:
                    index = k - (int)(o / 2)
                    vectorEven[l - 1] += x[k - l]*z[index]
                    vectorOdd[l - 1] += z[k - l]*z[index]
        print("vector Even \n ", vectorEven)
        print("vector Odd \n ", vectorOdd)
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
        print(out)

    #for i in range(deepness):
    #    for j in range(deepness):
    #        out


    return out


deepness = 2
featureSize = 7

x =np.array([2, 4, 1, 3, 1, 2, 4], np.float)
z =np.array([2, 1, 1, 2, 2, 3, 4], np.float)
z_hat = np.zeros(shape=(4, featureSize))
computeC (x, z, featureSize, deepness)


# finite difference model
#def computeDiffDepth():# computes optimal depth of model


