import time
#These are Metric => Imperial.
#---------------------------------------------
def millimeters_To_Inches(x):
    return x / 25.4

def meters_To_Feet(x):
    return x / 0.3048

def meters_To_Yards(x):
    return x / 0.9144

def kilometers_To_Miles(x):
    return x / 1.60934

#These are Imperial => Metric.
#---------------------------------------------
def inches_To_Millimeters(x):
    try:
        return x * 25.4
    except Exception:
        print("You can only input numbers!")
        time.sleep(5)
    
def feet_To_Meeters(x):
    return x * 0.3048

def yards_To_Meters(x):
    return x * 0.9144

def miles_To_Kilometers(x):
    return x * 1.60934


