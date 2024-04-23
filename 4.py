import numpy as np
import pandas as pd
from math import log,exp
from matplotlib import pyplot as plt
info=pd.DataFrame()
x=[]
y=[]
i=2
avrg=0
min=max=log(abs(1.3+i))-exp(i)
while (i<=3):
    x.append(i)
    i+=0.05
    y.append(log(abs(1.3+i))-exp(i))
    if(min>y[y.__len__()-1]):
        min=y[y.__len__()-1]
    if (max < y[y.__len__() - 1]):
        max = y[y.__len__() - 1]
    avrg+=y[y.__len__() - 1]

print(x)
print(y)
print("Min=", min)
print("Max=", max)
print("Avr=", avrg/(y.__len__() - 1))
x1=[]
y1=[]
x1.append(x[0])
x1.append(x[x.__len__() - 1])
y1.append (avrg/(y.__len__() - 1))
y1.append (avrg/(y.__len__() - 1))
info_dictionary={"x":x,"y":y}
info=pd.DataFrame(info_dictionary)
print(info)
plt.plot(info["x"],info["y"],label="f(x)")
plt.plot(x1,y1,label="avrg")
plt.title("График функций")
plt.xlabel("Переменная x")
plt.ylabel("Функция f(x)")
plt.legend(labels=["f(x)","avrg"])
plt.show()