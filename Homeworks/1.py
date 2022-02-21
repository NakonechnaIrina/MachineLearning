import time
import numpy as np
import random
n=50
array = np.random.randint((n,n))

def matrix_multiplic(a,b,n):

    x=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            
            for k in range(n):
                x[i][j]+=a[i][k]*b[k][j]
    return x[i][j]
def MulMat(a,b)
   x=np.dot(a,b)
   return x

print(' 1 algorithm: \n ')
%timeit MulMat(array,array)

print(' \t 2 algorithm: \n')
%timeit matrix_multiplic (array,array,n)
