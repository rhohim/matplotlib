# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 19:30:12 2019

@author: dull-dekstop
"""

import csv
import pandas as pd
from matplotlib import pyplot as plt 

#Untuk Mengambil Data Mpg dari file "mtcars - Data.csv"
def get_mpg():
    mpg = []
    f = open('mtcars - Data.csv', 'r')
    reader = csv.reader(f)
    for row in reader:
        mpg.append(row[1])
    f.close()
    del mpg[0]
    mpg = [float(i) for i in mpg]
    return mpg

#untuk memberi level sesuai dengan aturan yang ditetapkan
def get_mpg_level(mpg):
    level = []
    for i in range(0,len(mpg)):
        if mpg[i] < 20:
            level.append("Low")
        elif mpg[i] >=20 and mpg[i] <= 30:
            level.append("Medium")
        else:
            level.append("Hard")
    return level

#untuk mendapatkan nilai persentase dari setiap level
def get_percentage(level):
    
    L,M,H = 0,0,0
    for i in range(0,len(level)):
        if level[i] == 'Low':
            L=L+1
        elif level[i] == 'Medium':
            M=M+1
        else:
            H=H+1
    Low = (((L/32)*100)/100)
    Medium = (((M/32)*100)/100)
    Hard = (((H/32)*100)/100)
    return [L,Low,M,Medium,H,Hard]

#untuk mendapatkan scatterplot
def get_scatter_plot(plot):
    x = ["Low", "Medium", "Hard"]
    y = [plot[1],plot[3],plot[5]]
    plt.title("ScatterPlot")
    plt.xlabel("mpg_level")
    plt.ylabel("Percentage(%)")
    plt.scatter(x,y)
    plt.show()
    
#untuk mendapatkan barchart
def get_barchart_plot(plot):
    x = ["Low", "Medium", "Hard"]
    y = [plot[1],plot[3],plot[5]]
    plt.title("Barchart")
    plt.xlabel("mpg_level")
    plt.ylabel("Percentage(%)")
    plt.bar(x,y)
    plt.show()

#untuk mendapatkan lineplot    
def get_lineplot_plot(plot):
    x = ["Low", "Medium", "Hard"]
    y = [plot[1],plot[3],plot[5]]
    plt.title("Lineplot")
    plt.xlabel("mpg_level")
    plt.ylabel("Percentage(%)")
    plt.plot(x,y,'g--d')
    plt.show()

#untuk mendapatkan crosstab    
def get_crosstab(plot):
    mpg = get_mpg()
    level = get_mpg_level(get_mpg())
    dt = pd.DataFrame({'mpg':mpg,'Level':level})
    ct = pd.crosstab(dt.mpg, dt.Level,margins=True)
    print(ct)
    
#Data "mtcars - Data.csv" ditambahkan mpg_level lalu disimpan dengan nama 'result_mtcars - Data.csv'    
level = get_mpg_level(get_mpg())
percentage = get_percentage(level)
df = pd.read_csv('mtcars - Data.csv')
df['mpg_level'] = level
df.to_csv('result_mtcars - Data.csv', index=False)

#untuk mendapatkan scatterplot
get_scatter_plot(percentage)
#untuk mendapatkan barchart
get_barchart_plot(percentage)
#untuk mendapatkan lineplot
get_lineplot_plot(percentage)
#untuk mendapatkan crosstab 
get_crosstab(percentage)    