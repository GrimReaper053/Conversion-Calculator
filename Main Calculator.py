from Conversions import Area, Length, Mass, Pressure, Speed, Temperature, Volume, Liquid, calculator
import time

do_You_Want_To_Continue = ""

def get_conversion_choice():
    return input("""
[1]: Convert Imperial to Metric
[2]: Convert Metric to Imperial

Please enter your choice here: """)

def user_input():
    try:
        return float(input("Please input the number you would like to convert: "))
    except Exception:
        print("Invalid input you can only input numbers.")
    

what_Conversion_They_Use = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
 
while do_You_Want_To_Continue != "n":
    what_Conversion = input("""
Hi Thank you for using my conversion calculator what would you like to do 
[1]: Length
[2]: Area
[3]: Mass
[4]: Volume
[5]: Liquid
[6]: Speed
[7]: Temperature
[8]: Pressure
[9]: Mathematics Calculator

Please enter your choice here: """)
    
    if what_Conversion in what_Conversion_They_Use:
        if what_Conversion == "1":
            imperial_or_metric = get_conversion_choice()
            if imperial_or_metric == "1":
                length_metric = input("""
[1]: Inches to Millimeters
[2]: Feet to Meters
[3]: Yards to Meters
[4]: Miles to Kilometers

Please enter your choice here: """)
                
                if length_metric == "1":
                    try:
                        print(Length.inches_To_Millimeters(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
                elif length_metric == "2":
                    try:
                        print(Length.feet_To_Meeters(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
                elif length_metric == "3":
                    try:
                        print(Length.yards_To_Meters(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
                elif length_metric == "4":
                    try:
                        print(Length.miles_To_Kilometers(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
            elif imperial_or_metric == "2":
                length_Imperial = input("""
[1]: Millimeters to Inches:
[2]: Meters to Feet:
[3]: Meters to Yards:
[4]: Kilometers to Miles:

Please enter your choice here: """)
                
                if length_Imperial == "1":
                    try:
                        print(Length.millimeters_To_Inches(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
                    
                elif length_Imperial == "2":
                    try:
                        print(Length.meters_To_Feet(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
                elif length_Imperial == "3":
                    try:
                        print(Length.meters_To_Yards(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
                elif length_Imperial == "4":
                    try:
                        print(Length.kilometers_To_Miles(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
            else:
                print("Invalid input")
                continue
        elif what_Conversion == "2":
            imperial_or_metric = get_conversion_choice()
            if imperial_or_metric == "1":
                area_Metric = input("""
[1]: Square Inches to Square Centimeters
[2]: Square Feet to Square Meters
[3]: Square Yards to Square Meters
[4]: Acres to Hectares
[5]: Square Miles to Square Kilometers

Please enter your choice here: """)
                
                if area_Metric == "1":
                    try:
                        print(Area.square_Inches_To_Square_Centimeters(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
                elif area_Metric == "2":
                    try:
                        print(Area.square_Feet_to_Square_Meters(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
                elif area_Metric == "3":
                    try:
                        print(Area.square_Yards_To_Square_Meters(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
                elif area_Metric == "4":
                    try:
                        print(Area.acres_Hectares(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
                elif area_Metric == "5":
                    try:
                        print(Area.square_Miles_To_Square_Kilometers(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
            elif imperial_or_metric == "2":
                area_Imperial = input("""
[1]: Square Centimeters to Square Inches:
[2]: Square Meters to Square Feet:
[3]: Square Meters to Square Yards:
[4]: Hectares to Acres:
[5]: Square Kilometers to Square Miles:

Please enter your choice here: """)
                
                if area_Imperial == "1":
                    try:
                        print(Area.square_Centimeters_To_Square_inches(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
                elif area_Imperial == "2":
                    try:
                        print(Area.square_Meters_To_Square_Feet(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
                elif area_Imperial == "3":
                    try:
                        print(Area.Square_Meters_To_Square_Yards(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
                elif area_Imperial == "4":
                    try:
                        print(Area.hectares_To_Acres(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
                elif area_Imperial == "5":
                    try:
                        print(Area.square_Kilometers_To_Square_MilesSS(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
            else:
                print("Invalid input")
                continue
        elif what_Conversion == "3":
            imperial_or_metric = get_conversion_choice()
            if imperial_or_metric == "1":
                mass_Metric = input("""
[1]: Ounces to Grams:
[2]: Pounds to Kilograms
[3]: (US) Tons to Metric Tons

Please enter your choice here: """)
                if mass_Metric == "1":
                    try:
                        print(Mass.ounces_To_Grams(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
                elif mass_Metric == "2":
                    try:
                        print(Mass.pounds_To_Kilograms(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
                elif mass_Metric == "3":
                    try:
                        print(Mass.US_ton_To_Metric_ton(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
            elif imperial_or_metric == "2":
                mass_Imperial = input("""
[1]: Grams to Ounces
[2]: Kilograms to Pounds
[3]: Metric Tons to US Tons

Please enter your choice here: """)
                if mass_Imperial == "1":
                    try:
                        print(Mass.grams_To_Ounces(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
                elif mass_Imperial == "2":
                    try:
                        print(Mass.kilograms_To_Pounds(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
                elif mass_Imperial == "3":
                    try:
                        print(Mass.Metric_Ton_To_US_Ton(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
            else:
                print("Invalid input")
                continue
        elif what_Conversion == "4":
            imperial_or_metric = get_conversion_choice()
            if imperial_or_metric == "1":
                volume_Metric = input("""
[1]: Cubic Inches to Cubic Centimeters
[2]: Cubic Feet to Cubic Meters
[3]: Cubic Yards to Cubic Meters

Please enter your choice here: """)
                if volume_Metric == "1":
                    try:
                        print(Volume.cubic_Inches_To_Cubic_Centimeters(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
                elif volume_Metric == "2":
                    try:
                        print(Volume.cubic_Feet_To_Cubic_Meters(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
                elif volume_Metric == "3":
                    try:
                        print(Volume.cubic_Yards_To_Cubic_Meters(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
            elif imperial_or_metric == "2":
                volume_Imperial = input("""
[1]: Cubic Centimeters to Cubic Inches:
[2]: Cubic Meters to Cubic Feet:
[3]: Cubic Meters to Cubic Yards:

Please enter your choice here: """)
                if volume_Imperial == "1":
                    try:
                        print(Volume.cubic_Centimeters_To_Cubic_inches(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
                elif volume_Imperial == "2":
                    try:
                        print(Volume.cubic_Meters_To_Cubic_Feet(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
                elif volume_Imperial == "3":
                    try:
                        print(Volume.cubic_Meters_To_Yards(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
            else:
                print("Invalid input")
                continue
        elif what_Conversion == "5":
            imperial_or_metric = get_conversion_choice()
            if imperial_or_metric == "1":
                liquid_Metric = input("""
[1]: Fluid Ounces to Milliliters
[2]: Cups to Milliliters:
[3]: Pints to Liters:
[4]: Quarts to Liters:
[5]: Gallons to Liters:

Please enter your choice here: """)
                if liquid_Metric == "1":
                    try:
                        print(Liquid.fluid_Ounces_To_Milliliters(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
                elif liquid_Metric == "2":
                    try:
                        print(Liquid.cups_To_Milliliters(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
                elif liquid_Metric == "3":
                    try:
                        print(Liquid.pints_To_Liters(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
                elif liquid_Metric == "4":
                    try:
                        print(Liquid.quarts_To_Liters(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
                elif liquid_Metric == "5":
                    try:
                        print(Liquid.gallons_To_Liters(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
            elif imperial_or_metric == "2":
                liquid_Imperial = input("""
[1]: Milliliters to Fluid Ounces:
[2]: Milliliters to Cups:
[3]: Liters to Pints:
[4]: Liters to Quarts:
[5]: Liters to Gallons:

Please enter your choice here: """)
                if liquid_Imperial == "1":
                    try:
                        print(Liquid.milliliters_To_Fluid_Ounces(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
                elif liquid_Imperial == "2":
                    try:
                        print(Liquid.milliliters_To_Cups(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
                elif liquid_Imperial == "3":
                    try:
                        print(Liquid.liters_To_Pints(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
                elif liquid_Imperial == "4":
                    try:
                        print(Liquid.liters_To_Quarts(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
                elif liquid_Imperial == "5":
                    try:
                        print(Liquid.liters_To_Gallons(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
                    
            else:
                print("Invalid input")
                continue
        elif what_Conversion == "6":
            imperial_or_metric = get_conversion_choice()
            if imperial_or_metric == "1":
                speed_metric = input("""
[1]: Miles per Hour to Kilometers per Hour:
[2]: Feet per Second to Meters per Second:

Please enter your choice here: """)
                
                if speed_metric == "1":
                    try:
                        print(Speed.miles_Per_Hour_To_Kilometers_Per_Hour(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
                elif speed_metric == "2":
                    try:
                        print(Speed.feet_Per_Second_To_Meter_Per_Hour(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
            elif imperial_or_metric == "2":
                speed_imperial = input("""
[1]: Kilometers per Hour to Miles per Hour:
[2]: Meters per Second to Feet per Second:

Please enter your choice here: """)
                
                if speed_metric == "1":
                    try:
                        print(Speed.Kilometers_Per_Hour_To_Miles_Per_Hour(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
                elif speed_metric == "2":
                    try:
                        print(Speed.meters_Per_Second_To_Feet_Per_Second(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
            else:
                print("Invalid input")
                continue
        elif what_Conversion == "7":
            imperial_or_metric = get_conversion_choice()
            if imperial_or_metric == "1":
                temperature_metric = input("""
[1]: Celsius

Please enter your choice here: """)
                
                if temperature_metric == "1":
                    try:
                        print(Temperature.fahrenheit_To_Celsius(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
            elif imperial_or_metric == "2":
                temperature_imperial = input("""
[1]: Fahrenheit 

Please enter your choice here: """)
                
                if temperature_imperial == "1":
                    try:
                        print(Temperature.Celsius_To_Fahrenheit(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
            else:
                print("Invalid input")
                continue
        elif what_Conversion == "8":
            imperial_or_metric = get_conversion_choice()
            if imperial_or_metric == "1":
                Pressure_metric = input("""
[1]: Pounds per Square Inch (psi) to Pascals:

Please enter your choice here: """)
                
                if Pressure_metric == "1":
                    try:
                        print(Pressure.Pounds_Per_Square_Inch_To_Pascals(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
            elif imperial_or_metric == "2":
                Pressure_imperial = input("""
[1]:  Pascals to Pounds per Square Inch:

Please enter your choice here: """)
                
                if Pressure_imperial == "1":
                    try:
                        print(Pressure.Pascals_To_Pounds_Per_Square_Inch(user_input()))
                    except Exception:
                        print("Invalid Input. Numbers Or Decimals Only!")
                        time.sleep(1)
                        continue
            else:
                print("Invalid input")
                continue
        elif what_Conversion == "9":
            calculator.mathematics()
    elif what_Conversion not in what_Conversion_They_Use:
         print("Invalid Input!") 
         continue
    do_You_Want_To_Continue = input("Would you like to continue using the calculator (y/n): ")