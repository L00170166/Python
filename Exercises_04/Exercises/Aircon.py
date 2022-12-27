'''
Script: Aircon.py
By: CF
Purpose: Converts Temp 
Prerequisites: 
Tested: on Python v3.10.7 under Windows 11
Revision History:
Notes:
Do not edit the values in this script, all fixed settings are maintained at .\settings\Budget.py
This script has no error handling, by design.
'''
#CONVERT KELVN TO CELSIUS
print("Exercise Convert Kelvin to Celsius")
#conversion Kelvin to Celsius
conversion = 272.15
#list of temp in kelvin
my_temperature_in_kelvin = [200.01, 210.02, 220.05, 230.15, 240.20, 250.30, 200.40, 260.40, 200,40, 206.60]
#list in celsius by taking each temperature and substracting 
my_temperature_in_celsius = [(temperature - conversion) for temperature in my_temperature_in_kelvin]
#print celsius
print(my_temperature_in_celsius)
print()


#KELVN TO FAHRENHEIT
print("Exercise Convert Kelvin to Fahrenheit")
#conversion factor
conversion = 273.15
#list of temperature in kelvin
my_temperature_in_kelvin = [200.01, 210.02, 220.05, 230.15, 240.20, 250.30, 200.40, 260.40, 200,40, 206.60]
#create a list in fahrenheit by subsracting conversion
my_temperature_in_fahrenheit = [(temperature - conversion) * 1.8 + 32 for temperature in my_temperature_in_kelvin]
print(my_temperature_in_fahrenheit)
