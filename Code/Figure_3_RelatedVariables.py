import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

regions=["YRD","MAD","IWI","SP","CT","NSW"]
labels=["RH","VPD","TEMP","LR","PET","LH","HFX"]
rhs,vpds,temps,prs,pets,lhs,hfxs=[],[],[],[],[],[],[]
for region in regions:
    rhs.append(pd.read_csv("../Data/Figure 3/"+region+"/RH.csv").values[:,0])
    vpds.append(pd.read_csv("../Data/Figure 3/"+region+"/VPD.csv").values[:,0])
    temps.append(pd.read_csv("../Data/Figure 3/"+region+"/TEMP.csv").values[:,0])
    prs.append(pd.read_csv("../Data/Figure 3/"+region+"/LR.csv").values[:,0])
    pets.append(pd.read_csv("../Data/Figure 3/"+region+"/PET.csv").values[:,0])
    lhs.append(pd.read_csv("../Data/Figure 3/"+region+"/LH.csv").values[:,0])
    hfxs.append(pd.read_csv("../Data/Figure 3/"+region+"/HFX.csv").values[:,0])
vals=[rhs,vpds,temps,prs,pets,lhs,hfxs]

colors=["#aab18c","#d88da2","#f89c53","#899cb8","#e6bc28","#9d85c1"]
facecolors=["#dbd9cb","#faa3bb","#f8c39a","#adc5e8","#ffde69","#cfb0ff"]
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rc('font',family='Arial')
plt.figure(figsize=(24,9))
plt.subplots_adjust(hspace=0.45)
for pnum in range(1,8,1):
    plt.subplot(3,3,pnum)
    bp=plt.boxplot(vals[pnum-1],showfliers=False,patch_artist=True,whiskerprops={'linestyle':'--','linewidth':2},
                  boxprops={'facecolor':'none'},widths=0.6)
    plt.xticks([1,2,3,4,5,6],regions)
    plt.tick_params(labelsize=26)
    plt.title(labels[pnum-1],size=26,fontweight="bold")
    for i in range(len(bp['boxes'])):
        bp['boxes'][i].set(edgecolor=colors[i])
        bp['boxes'][i].set(linewidth=2)
        bp['boxes'][i].set(facecolor=facecolors[i])
        bp['medians'][i].set(color=colors[i])
        bp['medians'][i].set(linewidth=2)  
    if pnum!=6:
        plt.axhline(y=0, color='grey', linestyle='dashed',linewidth=2)
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
    if pnum==1 or pnum==4 or pnum==7:
        plt.ylabel("Change Rate",size=26)
plt.show()