import numpy as np
import pandas as pd
from math import log,exp
from matplotlib import pyplot as plt
y=np.linspace(1,5,20)
x=y
z1=[]
z2=[]
z3=[]
z4=[]
z5=[]
print(x)
print(y.__len__())
for i in range(y.__len__()):
    z1.append(pow(x[i],0.25)+pow(y[i],0.25))
    z2.append(pow(x[i], 2) - pow(y[i], 2))
    z3.append(2*x[i]+3*y[i])
    z4.append(pow(x[i], 2) + pow(y[i], 2))
    z5.append(2+2*x[i]+2*y[i]-pow(x[i], 2) - pow(y[i], 2))
fig=plt.figure()
ax1=fig.add_subplot(2,3,1,projection="3d")
ax2=fig.add_subplot(2,3,2,projection="3d")
ax3=fig.add_subplot(2,3,3,projection="3d")
ax4=fig.add_subplot(2,3,4,projection="3d")
ax5=fig.add_subplot(2,3,5,projection="3d")
ax1.plot(x,y,z1)
ax2.plot(x,y,z2)
ax3.plot(x,y,z3)
ax4.plot(x,y,z4)
ax5.plot(x,y,z5)
plt.show()