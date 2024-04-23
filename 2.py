import numpy as np
import random
x=np.ones((12,3))
y=np.ones((12,1))
z=np.ones((12,1))
for i in range(12):
    x[i][1]=random.randint(19,31)
    x[i][2] = random.randint(60, 82)
    y[i][0]=random.uniform(13.5, 18.6)
print(x)
c=x.transpose()
a1=np.linalg.matrix_power(c.dot(x),-1)
a2=c.dot(y)
a=a1.dot(a2)
print(a)
print(y)
for i in range(12):
    z[i][0]=a[0]+a[1]*x[i][1]+a[2]*x[i][2]
print(z)