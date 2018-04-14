import math
def cylinder_volume(R, L):
    return math.pi*(R**2)*L

print('for R = 3, L = 5 cylinder volume =', cylinder_volume(3,5))

def cylinder_square(R):
    return math.pi*(R**2)
print('for R = 3 cylinder square =', cylinder_square(3))
