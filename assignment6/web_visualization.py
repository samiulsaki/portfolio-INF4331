"""
@author: samiulsaki
Web Visualisation using python flask app
"""
import base64
from time import time
from flask import Flask, render_template, request
from temperature_CO2_plotter import plot_temperature, plot_CO2_country, plot_CO2_global,\
                                    tempYearMin, tempYearMax, globalCO2YearMin, globalCO2YearMax
app = Flask(__name__)

def _int(input):
	"""
    This function returns an input in to integer value and in to None 
    if input is an empty string.
    """
	if input == "":
		return None
	return int(input)

def _float(input):
	"""
    This function returns an input in to float value and in to None 
    if input is an empty string.
    """
	if input == "":
		return None
	return float(input)

def _str(input):
	"""
    This function returns an input in to string value and in to None 
    if input is an empty string.
    """
	if input == "":
		return None
	return str(input)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/help")
def help():
    """
    Returns to the help page
    """
    return render_template("help.html")

@app.route("/co2_global", methods=["POST", "GET"])
def co2_global():
    """
    Takes the given aguments from the user and creates plot with plot_CO2_global and 
    returns it to co2_global_page.html
    """
    if request.method == "GET":
        return render_template("co2_global_page.html", yearMin=globalCO2YearMin, yearMax=globalCO2YearMax)
    start = request.form["start"]
    end = request.form["end"]
    minY = request.form["minY"]
    maxY = request.form["maxY"]
    args  = [_int(start),_int(end),_float(minY),_float(maxY)]
    plots = [base64.b64encode(p.getvalue()).decode("ascii") for p in plot_CO2_global(*args)]
    return render_template("co2_global_page.html", plots=plots, yearMin=globalCO2YearMin, yearMax=globalCO2YearMax, 
                            x1=start, x2=end, y1=minY, y2=maxY)

@app.route("/temperature", methods=["POST", "GET"])
def temperature():
    """
    Takes the given aguments from the user and creates plot with plot_temperature and 
    returns it to temperature_page.html
    """
    if request.method == "GET":
        return render_template("temperature_page.html", yearMin=tempYearMin, yearMax=tempYearMax)
    month = request.form["month"]
    start = request.form["start"]
    end = request.form["end"]
    minY = request.form["minY"]
    maxY = request.form["maxY"]
    args  = [_str(month),_int(start),_int(end),_float(minY),_float(maxY)]
    plots = [base64.b64encode(p.getvalue()).decode("ascii") for p in plot_temperature(*args)]
    return render_template("temperature_page.html", plots=plots, yearMin=tempYearMin, yearMax=tempYearMax, 
                            m=month,x1=start, x2=end, y1=minY, y2=maxY)

@app.route("/co2_country", methods=["POST", "GET"])
def co2_country():
    """
    Takes the given aguments from the user and creates plot with plot_CO2_country and 
    returns it to co2_country_page.html
    """
    if request.method =="GET":
        return render_template("co2_country_page.html", yearMin=1960, yearMax=2016)
    year = request.form["year"]
    up = request.form["up"]
    low = request.form["low"]
    args = [_int(year),_float(up),_float(low)]
    plots = [base64.b64encode(p.getvalue()).decode("ascii") for p in plot_CO2_country(*args)]
    return render_template("co2_country_page.html", plots=plots, yearMin=1960, yearMax=2016, 
                            y = year, b1=up, b2=low)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')