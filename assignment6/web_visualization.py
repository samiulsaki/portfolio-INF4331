from flask import Flask, render_template, request
from temperature_CO2_plotter import plot_temperature, plot_CO2_country, plot_CO2_global, \
                                    tempYearMin,tempYearMax, globalCO2YearMin, globalCO2YearMax

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/co2_global", methods=["GET", "POST"])
def co2_global():
    if request.method == "GET":
        return render_template("co2_global.html", yearMin=globalCO2YearMin, yearMax=globalCO2YearMax)
    
    start = request.form["start"]; end = request.form["end"]
    minY = request.form["minY"]; maxY = request.form["maxY"]

    plots= plot_CO2_global(int(start),int(end),float(minY),float(maxY))
    plots = [base64.b64encode(p.getvalue()).decode("ascii") for p in plots]
    return render_template("co2_global.html",plots=plots, yearMin=globalCO2YearMin, 
                            yearMax=globalCO2YearMax, x1=start, x2=end, y1=minY, y2=maxY)

if __name__ == "__main__":
    app.run(debug=True)