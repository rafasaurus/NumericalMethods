import numpy as np

def computeC(x,z,featureSize,deepness):
    out = np.zeros(shape=(deepness*2,deepness*2))
    vectorEven = np.zeros(shape=(deepness))
    vectorOdd = np.zeros(shape=(deepness))
      # i

    for k in range(deepness, featureSize+1):
        print(k)
        for l in range(1,deepness+1):  # j
            vectorEven[l-1] +=  x[k - l]
            vectorOdd[l-1] += z[k - l]
                #print(vectorEven[l])
    #for i in range(deepness*2):
    #    for j in range(deepness*2):


    print("vector Even \n ",vectorEven)
    print("vector Odd \n ", vectorOdd)
    vector =vectorEven + vectorOdd

    return out

deepness = 3
featureSize = 7

x =np.array([2, 4, 1, 3, 1, 2, 4], np.float)
z =np.array([2, 1, 1, 2, 2, 3, 4], np.float)
z_hat = np.zeros(shape=(4, featureSize))
computeC (x, z, featureSize, deepness)


# finite difference model
#def computeDiffDepth():# computes optimal depth of model


