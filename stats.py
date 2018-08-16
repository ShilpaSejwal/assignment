#1

import numpy as np
a = np.random.rand(10,1)
print(a)
print("mean is",np.mean(a))

#2

import numpy as np
b = np.random.rand(20,1)
print(b)
print("variance is",np.var(b))
print("standard deviation ",np.std(b))

#3

import numpy as np
A = np.random.rand(10,20)
B = np.random.rand(20,25)
c = np.dot(A,B)
print(c)


#4

import numpy as np
a = np.arange(10).reshape(10,1)
print(a)
def func(x,axis):
    return 1/(1+np.exp(-x))
b = np.apply_over_axes(func,a,1)
print(b)



