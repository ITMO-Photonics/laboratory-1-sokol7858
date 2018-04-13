import numpy as np
import scipy.linalg as linalg

def task4(n,k):
    A=np.random.random((n,n))
    i,j=np.indices(A.shape)
    t=np.linspace(0.,10.,100)
    B=k/(1+k*t)
    return A, B

A, B=task4(100,1)

x1=linalg.solve(A,B)

x2=linalg.lu_solve(linalg.lu_factor(A),B,0)

x3=np.dot(linalg.inv(A),B)

print('solve_time')
get_ipython().run_line_magic('timeit', 'linalg.solve(A,B)')
print('lu_solve_time')
get_ipython().run_line_magic('timeit', 'linalg.lu_solve(linalg.lu_factor(A),B,0)')
print('dot_solve_time')
get_ipython().run_line_magic('timeit', 'np.dot(linalg.inv(A),B)')


