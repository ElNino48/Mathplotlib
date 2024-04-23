import numpy as np
import pandas as pd
import random
info=pd.read_csv("price_prepared.csv",sep=";")
print(info)
for i in range(info.shape[0]):
    if(info ["LifeSquare"][i]<0):
        info["LifeSquare"][i]=0
    if (info["KitchenSquare"][i] < 0):
        info["KitchenSquare"][i] = 0
    if (info["m_sq"][i] < 0):
        info["m_sq"][i] = 0
    info["Square"][i]= info["LifeSquare"][i]+info["KitchenSquare"][i]+info["m_sq"][i]
print(info)
