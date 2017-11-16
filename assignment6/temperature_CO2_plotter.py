import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

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

class EmptyData_ERROR(Exception):
	"""Empty DataFrame Error is raised when no data can be found for plotting"""
	pass

def plotify(title,xLabel,yLabel,minY,maxY):
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.legend()
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
    image = plotify(title,xLabel,yLabel,minY,maxY)
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
    image = plotify(title,xLabel,yLabel,minY,maxY)
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
    
    if up is None:
        max = round(1+tempData[year].max())
    else:
        max = round(1+up)
    min = 0
    
    
    # Plot the data
    #images = []
    nPerPlot = 30                #-- number of countries per plot
    nPlots = (len(tempData) // nPerPlot) #-- number of countries
    if nPlots == 0: nPlots = 1 #-- at least one plot must be plotted
    for i in range(nPlots):
        plt.figure()
        if i == nPlots: #-- last plot
            tempData[i*nPerPlot:].plot(x="Country Code", y=year, kind="barh")
        else:
            start = i*nPerPlot
            end = start + nPerPlot
            tempData[start:end].plot(x="Country Code", y=year, kind="barh")
            plt.xlabel("The CO2 Emissions (million tons per capita)")
            plt.xlim((min,max))
            plt.show()
            plt.close()
	
if __name__ == "__main__":
    plot_temperature('sep')
    plot_CO2_global()
    #plot_CO2_country(2000, up=None, low=10)