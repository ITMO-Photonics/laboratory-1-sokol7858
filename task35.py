import numpy as np


def task3(n):
    A=np.zeros((n,n))
    i,j=np.indices(A.shape)
    A[i,j]=i+j
    
    return A

A= task3(100)
print (A) 

