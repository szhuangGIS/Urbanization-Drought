import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter


regions=["YRD","MAD","IWI","SP","CT","NSW"]

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rc('font',family='Times New Roman')
plt.figure(figsize=(9,17))
plt.subplots_adjust(wspace=0.5)
num=0
colors=["#899cb8","#f89c53"]
facecolors=["#adc5e8","#f8c39a"]
for pnum in range(1,7,1):
    ax1=plt.subplot(3,2,pnum)
    data=pd.read_csv("../Data/Figure 2/"+regions[pnum-1]+"_Extreme.csv").values[:,0]
    bp=plt.boxplot([data],positions=[1],showfliers=False,patch_artist=True,whiskerprops={'linestyle':'--','linewidth':2},
                  boxprops={'facecolor':'none'},widths=0.6)
    ax1.axhline(y=0, color='#899cb8', linestyle='dashed',linewidth=3)
    plt.tick_params(labelsize=20)
    ax1.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    for i in range(len(bp['boxes'])):
        bp['boxes'][i].set(edgecolor=colors[i])
        bp['boxes'][i].set(linewidth=2)
        bp['boxes'][i].set(facecolor=facecolors[i])
        bp['medians'][i].set(color=colors[i])
        bp['medians'][i].set(linewidth=2)
    tnum=0
    for i in range(0,len(bp['whiskers']),2):
        bp['whiskers'][i].set(color=colors[tnum])
        bp['whiskers'][i].set(linewidth=2)
        bp['whiskers'][i+1].set(color=colors[tnum])
        bp['whiskers'][i+1].set(linewidth=2)
        bp['caps'][i].set(color=colors[tnum])
        bp['caps'][i+1].set(color=colors[tnum])
        bp['caps'][i].set(linewidth=2)
        bp['caps'][i+1].set(linewidth=2)
        tnum=tnum+1
    if pnum==1 or pnum==3 or pnum==5:
        plt.ylabel("Change Rate",size=23)
        
    ax2=ax1.twinx()
    data=pd.read_csv("../Data/Figure 2/"+regions[pnum-1]+"_Severity.csv").values[:,0]
    bp=plt.boxplot([data],positions=[2],showfliers=False,patch_artist=True,whiskerprops={'linestyle':'--','linewidth':2},
                  boxprops={'facecolor':'none'},widths=0.6)
    ax2.axhline(y=0, color='#f89c53', linestyle='dashed',linewidth=3)
    plt.tick_params(labelsize=20)
    ax2.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    for i in range(len(bp['boxes'])):
        bp['boxes'][i].set(edgecolor=colors[i+1])
        bp['boxes'][i].set(linewidth=2)
        bp['boxes'][i].set(facecolor=facecolors[i+1])
        bp['medians'][i].set(color=colors[i+1])
        bp['medians'][i].set(linewidth=2)
    plt.xlim(0.5,2.5)    
    plt.axvspan(xmin=0.5, xmax=1.5, facecolor="salmon", alpha=0.08)
    plt.axvspan(xmin=1.5, xmax=2.5, facecolor="lightblue", alpha=0.08)
    tnum=0
    for i in range(0,len(bp['whiskers']),2):
        bp['whiskers'][i].set(color=colors[tnum+1])
        bp['whiskers'][i].set(linewidth=2)
        bp['whiskers'][i+1].set(color=colors[tnum+1])
        bp['whiskers'][i+1].set(linewidth=2)
        bp['caps'][i].set(color=colors[tnum+1])
        bp['caps'][i+1].set(color=colors[tnum+1])
        bp['caps'][i].set(linewidth=2)
        bp['caps'][i+1].set(linewidth=2)
        tnum=tnum+1
    plt.xticks([1,2],["Extreme","Severity"],size=23)
    if pnum==2 or pnum==4 or pnum==6:
        plt.ylabel("Change Rate",size=23)
    num=num+1
    
plt.show()