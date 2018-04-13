import numpy as np
import scipy.linalg as linalg

def task3(n):
    A=np.zeros((n,n))
    i,j=np.indices(A.shape)
    B=np.zeros((n,1))
    A[i==j]=1
    A[i==j+1]=1
    A[i==j+2]=1
    for k in range(n):
        B[k,0]=k
    return A, B

A, B = task3(100)

solve=linalg.solve(A,B)


