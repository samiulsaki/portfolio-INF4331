"""
@author: samiulsaki
The python script with following functions:
(1) plotify: Creates a plot with given arguments
(2) 
"""

import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import numpy as np

countryCO2CSV = pd.read_csv('sources/CO2_by_country.csv', sep=',')
globalCO2CSV = pd.read_csv('sources/co2.csv', sep=',')
globalTempCSV = pd.read_csv('sources/temperature.csv', sep=',')

months = {
        "jan" : "January", 
        "feb" : "February", 
        "mar" : "March", 
        "apr" : "April", 
        "may" : "May", 
        "jun" : "June", 
        "jul" : "July", 
        "aug" : "August", 
        "sep" : "September", 
        "okt" : "October", 
        "nov" : "November", 
        "dec" : "December" }

tempYearMin = globalTempCSV["Year"].min()
tempYearMax = globalTempCSV["Year"].max()
globalCO2YearMin = globalCO2CSV["Year"].min()
globalCO2YearMax = globalCO2CSV["Year"].max()

def plotify(title,xLabel,yLabel,minY,maxY,minX,maxX):
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.legend()
    plt.xlim((minX,maxX))
    plt.ylim((minY, maxY))
    #plt.savefig('plots/imageTemp.png')
    #plt.show()
    image = BytesIO()
    plt.savefig(image, format="png")
    image.seek(0)
    return image

def plot_temperature(month, start=None, end=None, minY=None, maxY=None):
    if start != None:
        start = start - tempYearMin
    if end != None:
        end = end - tempYearMax-1
    month = months[month]
    tempData = globalTempCSV[start:end]

    if (minY != None) and (maxY != None):
        tempData = tempData[(tempData[month] >= minY) & (tempData[month] <= maxY)]
    elif minY != None:
        tempData = tempData[tempData[month] >= minY]
    elif maxY != None:
        tempData = tempData[tempData[month] <= maxY]
    
    
    # Plotting the data
    plt.figure()
    plt.plot(tempData["Year"],tempData[month], "-bo", markersize=3)
    title = ("The Temperature in All of " + month)
    xLabel = "Year"
    yLabel = "Temperature ($^\circ$C)"
    # plt.title("The Temperature in All of " + month)
    # plt.xlabel("Year")
    # plt.ylabel("Temperature ($^\circ$C)")
    # plt.legend()
    # plt.ylim((minY, maxY))
    # #plt.savefig('plots/imageTemp.png')
    # plt.show()
    image = plotify(title,xLabel,yLabel,minY,maxY,minX=None,maxX=None)
    plt.close()
    return [image]

def plot_CO2_global(start=None, end=None, minY=None, maxY=None):
    if start !=None:
        start = start - globalCO2YearMin
    if end != None:
        end = end - globalCO2YearMax-1

    tempData = globalCO2CSV[start:end]
    column = "Carbon"
    if (minY != None) and (maxY != None):
        tempData = tempData[(tempData[column] >= minY) & (tempData[column] <= maxY)]
    elif minY != None:
        tempData = tempData[tempData[column] >= minY]
    elif maxY != None:
        tempData = tempData[tempData[column] <= maxY]

    # Plotting the data
    plt.figure()
    plt.plot(tempData["Year"],tempData[column], "-r", markersize=3)
    title = ("The Fossil-Fuel CO2 Emissions (Globally)")
    xLabel = "Year"
    yLabel = "Emission"
    #plt.legend()
    #plt.ylim((minY, maxY))
    #plt.savefig('plots/imageCO2Global.png')
    #plt.show()
    image = plotify(title,xLabel,yLabel,minY,maxY,minX=None,maxX=None)
    plt.close()
    return [image]


def plot_CO2_country(year, up=None, low=None):
    year = str(year)
    tempData = countryCO2CSV[["Country Code", year]]
    #print(tempData)
    if (low !=None) and (up !=None):
        tempData = tempData[(tempData[year] >= low) & (tempData[year] <= up)]
    elif low !=None:
        tempData = tempData[tempData[year] >= low]
    elif up != None:
        tempData = tempData[tempData[year] <= up]
    minX = 0
    if up is None: maxX = round(1+tempData[year].max())
    else: maxX = round(1+up)
    
    # Plot the data
    images = []
    each_plot = 10                              # number of countries per plot
    total_plots = (len(tempData) / each_plot)   # number of countries
    #if total_plots == 0: total_plots = 1 #-- at least one plot must be plotted
    for i in np.arange(0,total_plots,1):        
        #plt.figure(figsize=(1,1))
        #plt.subplots(figsize=(17, 10))
        # if i == total_plots: #-- last plot
        #     tempData[i*each_plot:].plot(x="Country Code", y=year, kind="barh")
        # else:
        start = int(i) * each_plot
        end = start + each_plot
        tempData[start:end].plot(x="Country Code", y=year, kind="barh",color="black")
        #print(tempData[start:end])
        #plt.title ("The Fossil-Fuel CO2 Emissions (by Country)")
        title = "The Fossil-Fuel CO2 Emissions (by Country)"
        #plt.xlabel("CO2 Emission Level (metric tons per capita)")
        xLabel = "CO2 Emission Level (metric tons per capita)"
        yLabel= "Country Code"
        #print(start,end,min,max)
        #plt.xlim((min,max))
        images.append(plotify(title,xLabel,yLabel,minY=None,maxY=None,minX=minX,maxX=maxX))
        #plt.show()        
        plt.close()
    return images

if __name__ == "__main__":
    """
    The main module
    """
    plot_temperature('sep')
    plot_CO2_global()
    plot_CO2_country(1960, up=10, low=6)