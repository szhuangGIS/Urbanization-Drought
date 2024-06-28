import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

colors=["#809fbf","#f89f51","#d68fa7"]
width=0.6
ind=np.arange(1,7,1)
data=pd.read_csv("../Data/Figure 1/UE_Proportion.csv").values

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rc('font',family='Arial')
plt.figure(figsize=(27,5))
plt.subplots_adjust(wspace=0.15)
plt.subplot(1,2,1)
plt.bar(ind, data[:,0], width,color=colors[0],label='Type A',zorder=999)
plt.bar(ind, data[:,1], width, bottom=data[:,0],color=colors[1], label='Type B',zorder=999)
plt.bar(ind, data[:,2], width, bottom=data[:,0]+data[:,1],color=colors[2], label='Type B',zorder=999)
plt.xticks(ind,["Extreme\nSPEI","Heavy\nSPEI","Moderate\nSPEI","Light\nSPEI","Drought\nSeverity","Drought\nDuration"])
plt.ylabel("Proportion",size=30)
plt.tick_params(labelsize=30)
plt.ylim(0,1)
plt.grid(linestyle="--",axis="y",zorder=0)

plt.subplot(1,2,2)
plt.bar(ind, data[:,3], width,color=colors[0],label='Type A',zorder=999)
plt.bar(ind, data[:,4], width, bottom=data[:,3],color=colors[1], label='Type B',zorder=999)
plt.bar(ind, data[:,5], width, bottom=data[:,3]+data[:,4],color=colors[2], label='Type B',zorder=999)
plt.xticks(ind,["Extreme\nSPEI","Heavy\nSPEI","Moderate\nSPEI","Light\nSPEI","Drought\nSeverity","Drought\nDuration"])
plt.ylabel("Proportion",size=30)
plt.tick_params(labelsize=30)
plt.grid(linestyle="--",axis="y",zorder=0)
plt.ylim(0,1)

plt.show()