"""
@author: samiulsaki
The python script with following functions:
(1) plotify: Creates a plot with given arguments
(2) plot_temperature: Temperature (globally)
(3) plot_CO2_global: Fossil-Fuel CO2 Emissions (globally)
(4) plot_CO2_country: Fossil-Fuel CO2 Emissions (by country)
(5) CO2Extrapolate: Function used to extrapolate the CO2 levels
(6) predicting_future: Prediction of the Future of CO2 Level
"""

import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import numpy as np
import math
import scipy.optimize as opt

countryCO2CSV = pd.read_csv('sources/CO2_by_country.csv')
globalCO2CSV = pd.read_csv('sources/co2.csv')
globalTempCSV = pd.read_csv('sources/temperature.csv')

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
        "oct" : "October", 
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

        @param title        the title of the pyplot
        @param xLabel       the x-axis label of the pyplot
        @param yLabel       the y-axis label of the pyplot
        @param minY         the minimum limit of Y-axis
        @param maxY         the maximum limit of Y-axis
        @param minX         the minimum limit of X-axis
        @param maxX         the maximum limit of X-axis
        @return             returns image(pyplot) in a form of BytesIO object
    """
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.legend()
    plt.xlim((minX,maxX))
    plt.ylim((minY, maxY))
    image = BytesIO()
    plt.savefig(image, format="png")
    image.seek(0)
    return image

def plot_temperature(month, start=None, end=None, minY=None, maxY=None,show_plot=False):
    """
    This function plots a pyplot (scatter) of the global temperature in a given 
    time period from given data. It returns an image/pyplot figure as a BytesIO object.
 
        @param month        represents the first three letters of months in calender (e.g. jan, feb, mar ...)
        @param start        represents the first year in the pyplot
        @param end          represents the last year in the pyplot
        @param minY         represents the lower limit of Y axis (temperature) in the pyplot
        @param maxY         represents the upper limit of Y axis (temperature) in the pyplot
        @param show_plot    shows the pyplot if set to True
        @return             returns plyplot for the global temperature with given arguments
    """
    # Setting the first and last year in the pyplot
    if start != None: start = start - tempYearMin
    if end != None: end = (end - tempYearMax) - 1
    month = months[month]
    tempData = globalTempCSV[start:end]
    tempData = tempData.dropna()

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
    title = "The Temperature in All of " + month
    xLabel = "Year"
    yLabel = "Temperature ($^\circ$C)"
    
    # The plotify function is returning the image
    image = plotify(title,xLabel,yLabel,minY,maxY,minX=None,maxX=None)
    if show_plot: plt.show()
    plt.close()
    return [image]

def plot_CO2_global(start=None, end=None, minY=None, maxY=None,show_plot=False):
    """
    This function plots a pyplot of the global CO2 emissions in a given 
    time period from given data. It returns an image/pyplot figure as a BytesIO object.

        @param start        represents the first year in the pyplot
        @param end          represents the last year in the pyplot
        @param minY         represents the lower limit of Y axis (CO2 emission level) in the pyplot
        @param maxY         represents the upper limit of Y axis (CO2 emission level) in the pyplot
        @param show_plot    shows the pyplot if set to True
        @return             returns plyplot for the global CO2 emissions with given arguments
    """    
    # Setting the first and last year in the pyplot
    if start !=None: start = start - globalCO2YearMin
    if end != None: end = (end - globalCO2YearMax) - 1
    tempData = globalCO2CSV[start:end]
    tempData = tempData.dropna()

    # Setting the lower and upper limit of Y-axis
    column = "Carbon"
    if (minY != None) and (maxY != None):
        tempData = tempData[(tempData[column] >= minY) & (tempData[column] <= maxY)]
    elif minY != None:
        tempData = tempData[tempData[column] >= minY]
    elif maxY != None:
        tempData = tempData[tempData[column] <= maxY]
    
    # Plotting the data with the plotify function. The plotify function is returning the image
    plt.figure()
    plt.plot(tempData["Year"],tempData[column], "-r", markersize=3)
    title = "The Fossil-Fuel CO2 Emissions (Globally)"
    xLabel = "Year"
    yLabel = "CO2 Emission Level"
    image = plotify(title,xLabel,yLabel,minY,maxY,minX=None,maxX=None)
    if show_plot: plt.show()
    plt.close()
    return [image]

def plot_CO2_country(year, up=None, low=None,show_plot=False):
    """
    This function plots a bar chart of the Fossil-Fuel CO2 emissions of individual countries at 
    different years within the given preset threshold from given data. It returns a list of image/
    pyplot figures as a BytesIO object.

        @param year         represents the year that is set to be plotted in the pyplot
        @param up           upper boundary of the threshold (X-Axis) in the pyplot
        @param low          lower boundary of the threshold (X-axis) in the pyplot
        @param show_plot    shows the pyplot if set to True
        @return             returns plyplot(s) for the CO2 emission for the individual countries 
                            with given arguments
    """
    # Setting the year to be plotted in the pyplot
    year = str(year)
    tempData = countryCO2CSV[["Country Code", year]]
    tempData = tempData.dropna()    
    
    # Setting the upper and lower limit of X-axis
    if (low !=None) and (up !=None):
        tempData = tempData[(tempData[year] >= low) & (tempData[year] <= up)]
    elif low !=None:
        tempData = tempData[tempData[year] >= low]
    elif up != None:
        tempData = tempData[tempData[year] <= up]
    
    
    # Setting the lower and upper limit of Y-axis
    minX = 0
    if math.isnan(tempData[year].max()): maxX = round(0)
    elif up is None: maxX = round(1+tempData[year].max())
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
        tempData[start:end].plot(x="Country Code", y=year, kind="barh", color="black")
        title = "The Fossil-Fuel CO2 Emissions (by Country)"
        xLabel = "CO2 Emission Level (million metric tons per capita)"
        yLabel= "Country Code"
        images.append(plotify(title,xLabel,yLabel,minY=None,maxY=None,minX=minX,maxX=maxX))
        if show_plot: plt.show()
        plt.close()
    return images

def CO2Extrapolate(x, a, b, c, d, e):
    """
    The function used to extrapolate the CO2 levels (as a function of time).
    
        @param x            years
        @param a,b,c,d,e    parameters used for curve fitting
        @return             polynomial plus exponential value
    """
    return a + b * x + c * np.exp(d * (x - e))

def predicting_future(years, show_plot=False):
    """
    The function calculates and predicts the future of CO2 level over a given time (years) and returns them 
    in a form of pyplot. It is based on a making a best fit plot on the scattered data of CO2 (co2) and 
    temperature (temp). From that we are able to calculate our a + b * x + c * np.exp(d * (x - e)) and it 
    shows the future predicatable level of CO2 level in next given years in a form of a optimal curve. The estimation 
    of next few years are only based on best predication and to use for research purposes only.

        @param years        represents the years in the future the prediction will need to be calculated for
        @param show_plot    shows the pyplot if set to True
        @return             returns the pyplot with the predicted level of CO2 level in next future years 
                            (user defined)
    """
    co2_years = []
    co2 = []
    for i in globalCO2CSV["Year"]: co2_years.append(i)
    for i in globalCO2CSV["Carbon"]: co2.append(float(i))
    
    # Let scipy find the optimal parameters for the CO2(year) interpolation.
    CO2Optimal, CO2Cov = opt.curve_fit(CO2Extrapolate, co2_years, co2, bounds=([-100., 0., 0., 0., 0.], [100., 10., 3e-2, 3e-2, 2e3]))
    CO2WithYear = np.linspace(min(co2_years), max(co2_years) + years, len(co2_years) * 100)

    # Visualize CO2 as a function of time, and the extrapolation.
    plt.plot(co2_years, co2)
    plt.plot(CO2WithYear, CO2Extrapolate(CO2WithYear, *CO2Optimal))
    title = "Prediction of CO2 Level Over Next " + str(years) + " Years"
    xLabel = "Year"
    yLabel= "CO2 Level"
    image = plotify(title,xLabel,yLabel,minY=None,maxY=None,minX=None,maxX=None)
    if show_plot: plt.show()
    plt.close()
    return [image]

if __name__ == "__main__":
    """
    The main call function
    """
    plot_temperature('sep', show_plot=True)
    plot_temperature('mar', 1850, 2005, None, None, show_plot=True)
    plot_CO2_global(1876, 1991, show_plot=True)
    plot_CO2_country(2000, up=10, low=6, show_plot=True)
    predicting_future(years=10, show_plot=True)
