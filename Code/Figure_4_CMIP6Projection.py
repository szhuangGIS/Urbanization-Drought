import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

trenddata=pd.read_csv("../Data/Figure 4/Trend_Ensemble_Monthly.csv")
trenddata[["USlope","RSlope"]]=trenddata[["USlope","RSlope"]]*10000 # To improve legibility
sigs=trenddata[["UTrend","RTrend"]].values
trends=trenddata[["USlope","RSlope"]].values.astype(float)

formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((-1,1))
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rc('font',family='Arial')
fig=plt.figure(figsize=(30,20))
plt.subplots_adjust(hspace=0.2,wspace=0.45)
num=1
for region in range(0,30,1):
    data=pd.read_csv("../Data/Figure 4/"+str(region)+".csv").values
    urban=data[2:,0]
    rural=data[2:,1]
    useries=[np.mean(urban[:10])]
    rseries=[np.mean(rural[:10])]
    for i in range(10,len(urban),12):
        useries.append(np.mean(urban[i:i+12]))
        rseries.append(np.mean(rural[i:i+12]))
    useries=np.array(useries)*10 # To improve legibility
    rseries=np.array(rseries)*10 # To improve legibility
    
    ax1=plt.subplot(5,6,num) 
    plt.plot(useries,c="#899cb8",linewidth=3,label="Urban")
    plt.plot(rseries,c="#f89c53",linewidth=3,label="Rural")
    plt.xlim(-0.5,44)
    plt.axvline(x=36, linestyle='dashed', color='black')
    plt.axvspan(xmin=-0.5, xmax=36, facecolor="salmon", alpha=0.05)
    plt.axvspan(xmin=36, xmax=44, facecolor="lightblue", alpha=0.1)
    plt.tick_params(labelsize=32)
    plt.xticks(np.arange(0,36,10),np.arange(2015,2051,10))
    ax1.tick_params(axis='x', labelsize=26)
    ax1.yaxis.set_major_locator(ticker.MaxNLocator(integer=True,nbins=3))
    if region in [0,6,12,18,24]:
        plt.ylabel("SPEI",size=29)
    plt.legend(loc=3,fontsize=20)
    
    ax2=ax1.twinx()
    barval=[trends[region,0],trends[region,1]]
    if sigs[region,0]!="no trend":
        plt.bar([38.5],[trends[region,0]],width=2,color=["#899cb8"],edgecolor='black',hatch="/")
    else:
        plt.bar([38.5],[trends[region,0]],width=2,color=["#899cb8"],edgecolor='black')
    if sigs[region,1]!="no trend":
        plt.bar([41.7],[trends[region,1]],width=2,color=["#f89c53"],edgecolor='black',hatch="/")
    else:
        plt.bar([41.7],[trends[region,1]],width=2,color=["#f89c53"],edgecolor='black')
    plt.tick_params(labelsize=32)
    if region in [5,11,17,23,29]:
        plt.ylabel("Trend (per month)",size=29)
    plt.xticks([0,15,30,38,42],["2015","2030","2045","U","R"])
    ax2.yaxis.set_major_locator(ticker.MaxNLocator(integer=True,nbins=3))
    
    num=num+1
plt.show()