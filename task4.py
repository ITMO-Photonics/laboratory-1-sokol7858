import numpy as np
import scipy
import timeit
N = 50
A = np.random.random((N,N))
k = np.arange(N)
def b(k,t):
	return (k/(1+k*t))

start = timeit.default_timer()
for t in np.linspace(0,10,100):
	x1 = scipy.linalg.solve(A,b(k,t))
stop = timeit.default_timer()-start
print(stop)

start = timeit.default_timer()
LU = scipy.linalg.lu_factor(A)
for t in np.linspace(0,10,100):
	x2 = scipy.linalg.lu_solve(LU,b(k,t))
stop = timeit.default_timer()-start
print(stop)

start = timeit.default_timer()
Ainv = scipy.linalg.inv(A)
for t in np.linspace(0,10,100):
	x3 = np.dot(Ainv,b(k,t))
	stop = timeit.default_timer()-start
print(stop)