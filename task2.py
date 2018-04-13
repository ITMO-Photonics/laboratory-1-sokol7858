import numpy as np
import scipy.optimize as opt

def fun(x):
    return (np.cos(x)/(1+x**2))

#def fun1(x):
#    return -(((x**2+1)*np.sin(x)+2*x*np.cos(x))/((x**2+1)**2))

brentq_root=opt.brentq(fun,0.1,2.4)
bisect_root=opt.bisect(fun,0.1,2.4)
newton1_root=opt.newton(fun, 0.5, fprime = lambda x: -(((x**2+1)*np.sin(x)+2*x*np.cos(x))/((x**2+1)**2)))
newton2_root=opt.newton(fun, 0.5)

print('brentq_root =',brentq_root)
get_ipython().run_line_magic('timeit', 'opt.brentq(fun,0.1,2.4)')
print('bisect_root =',bisect_root)
get_ipython().run_line_magic('timeit', 'opt.bisect(fun,0.1,2.4)')
print('newton1_root =',newton1_root)
get_ipython().run_line_magic('timeit', 'opt.newton(fun, 0.5, fprime = lambda x: -(((x**2+1)*np.sin(x)+2*x*np.cos(x))/((x**2+1)**2)))')
print('newton2_root =',newton2_root)
get_ipython().run_line_magic('timeit', 'opt.newton(fun, 0.5)')

#%timeit -o opt.brentq(fun,0.1,2.4)
#%timeit -o opt.bisect(fun,0.1,2.4)
#%timeit -o opt.newton(fun, 0.5, fprime = lambda x: -(((x**2+1)*np.sin(x)+2*x*np.cos(x))/((x**2+1)**2)))
#%timeit -o opt.newton(fun, 0.5)





