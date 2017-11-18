import base64
from time import time
from flask import Flask, render_template, request
from temperature_CO2_plotter import plot_temperature, plot_CO2_country, plot_CO2_global,\
                                    tempYearMin, tempYearMax, globalCO2YearMin, globalCO2YearMax

app = Flask(__name__)

def _int(input):
	"""Converts input to 'int'. Returns None if input is an empty string."""
	if input == "":
		return None
	return int(input)

def _float(input):
	"""Converts input to 'float'. Returns None if input is an empty string."""
	if input == "":
		return None
	return float(input)

def _str(input):
	"""Converts input to 'float'. Returns None if input is an empty string."""
	if input == "":
		return None
	return str(input)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/co2_global", methods=["POST", "GET"])
def co2_global():
    if request.method == "GET":
        return render_template("co2_global_page.html", yearMin=globalCO2YearMin, yearMax=globalCO2YearMax)
    
    start = request.form["start"]
    end = request.form["end"]
    minY = request.form["minY"]
    maxY = request.form["maxY"]
    args  = [_int(start),_int(end),_float(minY),_float(maxY)]
    
    #try:
    plots = plot_CO2_global(*args)
        #print("Canari")
    # except EmptyData_ERROR:
    #     return render_template("co2_global_page.html", yearMin=globalCO2YearMin, yearMax=globalCO2YearMax,
    #                             x1=start, x2=end, y1=minY, y2=maxY, 
    #                             error="No data found! Please change the input arguments")
    plots = [base64.b64encode(p.getvalue()).decode("ascii") for p in plots]
    return render_template("co2_global_page.html", plots=plots, yearMin=globalCO2YearMin, yearMax=globalCO2YearMax, 
                            x1=start, x2=end, y1=minY, y2=maxY)

@app.route("/temperature", methods=["POST", "GET"])
def temperature():
    if request.method == "GET":
        return render_template("temperature_page.html", yearMin=tempYearMin, yearMax=tempYearMax)
    
    month = request.form["month"]
    start = request.form["start"]
    end = request.form["end"]
    minY = request.form["minY"]
    maxY = request.form["maxY"]
    args  = [_str(month),_int(start),_int(end),_float(minY),_float(maxY)]
    
    #try:
    plots = plot_temperature(*args)
        #print("Canari")
    # except EmptyData_ERROR:
    #     return render_template("co2_global_page.html", yearMin=globalCO2YearMin, yearMax=globalCO2YearMax,
    #                             x1=start, x2=end, y1=minY, y2=maxY, 
    #                             error="No data found! Please change the input arguments")
    plots = [base64.b64encode(p.getvalue()).decode("ascii") for p in plots]
    return render_template("temperature_page.html", plots=plots, yearMin=tempYearMin, yearMax=tempYearMax, 
                            m=month,x1=start, x2=end, y1=minY, y2=maxY)

@app.route("/co2_country", methods=["POST", "GET"])
def co2_country():
    if request.method =="GET":
        return render_template("co2_country_page.html", yearMin=1960, yearMax=2016)

    year = request.form["year"]
    up = request.form["up"]
    low = request.form["low"]
    args = [_int(year),_float(up),_float(low)]

    #plots = plot_CO2_country(*args)
    plots = [base64.b64encode(p.getvalue()).decode("ascii") for p in plot_CO2_country(*args)]
    
    return render_template("co2_country_page.html", plots=plots, yearMin=1960, yearMax=2016, 
                            y = year, b1=up, b2=low)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')