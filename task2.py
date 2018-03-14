import numpy as np
import scipy.optimize as opt

def fun(x)
    return (np.cos(x)/(1+n**2))

brentq_root=opt.brentq(fun,0.1,2.4)
bisect_root=opt.bisect(fun,0.1,2,4)
newton_root=opt.newton(fun, 0.1, (((x**2+1)*np.sin(x)+2*x*np.cos(x))/(x**2+1)**2)))
newton2_root=opt.newton(fun, 0.1)

brentq_time=%timeit -o opt.brentq(fun,0.,5.)

bisect_time=%timeit -o opt.bisect(fun,0.,5.)

newton_time=%timeit -o opt.newton(fun, 0.1, (((x**2+1)*np.sin(x)+2*x*np.cos(x))/(x**2+1)**2)))

newton2_time=%timeit -o opt.newton(fun, 0.1)
