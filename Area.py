#These are Metric => Imperial.
#---------------------------------------------
def square_Centimeters_To_Square_inches(x):
    return (x**2) / 6.4516

def square_Meters_To_Square_Feet(x):
    return (x**2) / 0.092903

def  Square_Meters_To_Square_Yards(x):
    return (x**2) / 0.836127

def hectares_To_Acres(x):
    return (x**2) / 0.404686

def square_Kilometers_To_Square_Miles(x):
    return (x**2) / 2.58999

#These are Imperial => Metric.
#---------------------------------------------
def square_Inches_To_Square_Centimeters(x):
    return (x**2) * 6.4516

def square_Feet_to_Square_Meters(x):
    return (x**2) * 0.092903

def square_Yards_To_Square_Meters(x):
    return (x**2) * 0.836127

def acres_Hectares(x):
    return (x**2) * 0.836127

def square_Miles_To_Square_Kilometers(x):
    return (x**2) * 0.258999
