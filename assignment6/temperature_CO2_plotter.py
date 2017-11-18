"""
@author: samiulsaki
The python script with following functions:
(1) plotify: Creates a plot with given arguments
(2) plot_temperature: Temperature (globally)
(3) plot_CO2_global: Fossil-Fuel CO2 Emissions (globally)
(4) plot_CO2_country: Fossil-Fuel CO2 Emissions (by country)
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
    """
    Creates and saves the pyplot image into a BytesIO object 
    and then returns it to thefunction
    """
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.legend()
    plt.xlim((minX,maxX))
    plt.ylim((minY, maxY))
    #plt.show()
    image = BytesIO()
    plt.savefig(image, format="png")
    image.seek(0)
    return image

def plot_temperature(month, start=None, end=None, minY=None, maxY=None):
    """
    This function plots a pyplot (scatter) of the global temperature in a given 
    time period from given data. It returns an image/pyplot figure as a BytesIO object.
    
    :type month: string
    :param month: represents the first three letters of months in calender (e.g. jan, feb, mar...)

    :type start: integer
    :param start: represents the first year in the pyplot

    :type end: integer
    :param end: represents the last year in the pyplot

    :type minY: float
    :param minY: represents the lower limit of Y axis (temperature) in the pyplot

    :type maxY: float
    :param maxY: represents the upper limit of Y axis (temperature) in the pyplot
    """
    # Setting the first and last year in the pyplot
    if start != None:
        start = start - tempYearMin
    if end != None:
        end = (end - tempYearMax) - 1
    month = months[month]
    tempData = globalTempCSV[start:end]
    
    # Setting the lower and upper limit of Y-axis
    if (minY != None) and (maxY != None):
        tempData = tempData[(tempData[month] >= minY) & (tempData[month] <= maxY)]
    elif minY != None:
        tempData = tempData[tempData[month] >= minY]
    elif maxY != None:
        tempData = tempData[tempData[month] <= maxY]    
    
    # Plotting the data with the plotify function
    plt.figure()
    plt.plot(tempData["Year"],tempData[month], "-bo", markersize=3)
    title = ("The Temperature in All of " + month)
    xLabel = "Year"
    yLabel = "Temperature ($^\circ$C)"
    
    # The plotify function is returning the image
    image = plotify(title,xLabel,yLabel,minY,maxY,minX=None,maxX=None)
    plt.close()
    return [image]

def plot_CO2_global(start=None, end=None, minY=None, maxY=None):
    """
    This function plots a pyplot of the global CO2 emissions in a given 
    time period from given data. It returns an image/pyplot figure as a BytesIO object.

    :type start: integer
    :param start: represents the first year in the pyplot

    :type end: integer
    :param end: represents the last year in the pyplot

    :type minY: float
    :param minY: represents the lower limit of Y axis (CO2 emission level) in the pyplot

    :type maxY: float
    :param maxY: represents the upper limit of Y axis (CO2 emission level) in the pyplot
    """
    
    # Setting the first and last year in the pyplot
    if start !=None:
        start = start - globalCO2YearMin
    if end != None:
        end = (end - globalCO2YearMax) - 1
    tempData = globalCO2CSV[start:end]
    
    # Setting the lower and upper limit of Y-axis
    column = "Carbon"
    if (minY != None) and (maxY != None):
        tempData = tempData[(tempData[column] >= minY) & (tempData[column] <= maxY)]
    elif minY != None:
        tempData = tempData[tempData[column] >= minY]
    elif maxY != None:
        tempData = tempData[tempData[column] <= maxY]
    
    # Plotting the data with the plotify function. The plotify function 
    # is returning the image
    plt.figure()
    plt.plot(tempData["Year"],tempData[column], "-r", markersize=3)
    title = ("The Fossil-Fuel CO2 Emissions (Globally)")
    xLabel = "Year"
    yLabel = "CO2 Emission Level"
    image = plotify(title,xLabel,yLabel,minY,maxY,minX=None,maxX=None)
    plt.close()
    return [image]

def plot_CO2_country(year, up=None, low=None):
    """
    This function plots a bar chart of the Fossil-Fuel CO2 emissions of individual countries at 
    different years within the given preset threshold from given data. It returns a list of image/
    pyplot figures as a BytesIO object.

    :type year: integer
    :param year: represents the year that is set to be plotted in the pyplot

    :type up: float
    :param up: upper boundary of the threshold (X-Axis) in the pyplot

    :type low: float
    :param low: lower boundary of the threshold (X-axis) in the pyplot
    """
    # Setting the year to be plotted in the pyplot
    year = str(year)
    tempData = countryCO2CSV[["Country Code", year]]
    
    # Setting the upper and lower limit of X-axis
    if (low !=None) and (up !=None):
        tempData = tempData[(tempData[year] >= low) & (tempData[year] <= up)]
    elif low !=None:
        tempData = tempData[tempData[year] >= low]
    elif up != None:
        tempData = tempData[tempData[year] <= up]    
    # Setting the lower and upper limit of Y-axis
    minX = 0
    if up is None: maxX = round(1+tempData[year].max())
    else: maxX = round(1+up)    

    # Setting the number of countries in each plot
    images = []
    each_plot = 10
    total_plots = (len(tempData) / each_plot)
    # Creates pyplots for given year with threshold
    for i in np.arange(0,total_plots,1):        
        # Set the upper and lower threshold for each individual pyplot
        start = int(i) * each_plot
        end = start + each_plot

        # Plotting the data with the plotify function. The plotify function is 
        # returning the image(s). Each image gets appended to images list
        tempData[start:end].plot(x="Country Code", y=year, kind="barh",color="black")
        title = "The Fossil-Fuel CO2 Emissions (by Country)"
        xLabel = "CO2 Emission Level (metric tons per capita)"
        yLabel= "Country Code"
        images.append(plotify(title,xLabel,yLabel,minY=None,maxY=None,minX=minX,maxX=maxX))
        plt.close()
    return images

if __name__ == "__main__":
    """
    The main call function
    """
    plot_temperature('sep')
    plot_temperature('mar', 1850, 2005, None, None)
    plot_CO2_global(1876,1991)
    plot_CO2_country(2000, up=10, low=6)