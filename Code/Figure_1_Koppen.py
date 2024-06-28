import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rc('font',family='Arial')
plt.figure(figsize=(20,5))
data=pd.read_csv("../Data/Figure 1/UE_Koppen.csv").values[:,1:]

ax1=plt.subplot(111)
#Extreme
plt.bar(np.arange(0,4,1),data[:,0],color=["#a4b68f","#d68fa7","#f89f51","#809fbf"])
plt.bar(np.arange(4,8,1),data[:,1],color=["#a4b68f","#d68fa7","#f89f51","#809fbf"])
plt.ylim(-0.2,0.2)
plt.tick_params(labelsize=24)
plt.ylabel("Mean UE",size=26)
plt.grid(linestyle="--",axis="y")
plt.axvspan(xmin=-1, xmax=8, facecolor="salmon", alpha=0.04)
plt.axvspan(xmin=8, xmax=17, facecolor="lightblue", alpha=0.04)
plt.xticks([1.5,5.5,10.5,14.5],["UE-Negative","UE-Positive","UE-Negative","UE-Positive"])
#Severity
plt.bar(np.arange(9,13,1),data[:,2],color=["#a4b68f","#d68fa7","#f89f51","#809fbf"])
plt.bar(np.arange(13,17,1),data[:,3],color=["#a4b68f","#d68fa7","#f89f51","#809fbf"])
plt.xlim(-0.5,16.5)
plt.tick_params(labelsize=30)
plt.ylabel("Mean UE",size=30)

plt.axvspan(xmin=-1, xmax=8, facecolor="salmon", alpha=0.04)
plt.axvspan(xmin=8, xmax=17, facecolor="lightblue", alpha=0.04)
plt.xticks([1.5,5.5,10.5,14.5],["UE-Negative","UE-Positive","UE-Negative","UE-Positive"])
plt.grid(linestyle="--",axis="y",zorder=999)
plt.show()
