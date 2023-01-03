'''
Script: fuel_consumption.py
By: CF
Purpose: Is to calculate Fuel consumption
Prerequisites: 
Tested: on Python v3.10.7 under Windows 11
Revision History:
Notes:
Do not edit the values in this script, all fixed settings are maintained at .\Python\Exercises_07\Exercises
This script has no error handling, by design.
'''
#def validate_integer():
#Amount of Fuel
fuel=4
#consumed
fuel_consumption=.50
#endurance
endurance =0
#60 seconds per min
per_minute =60
#print fuel  
print(fuel / fuel_consumption - endurance)
while False:
 try:
  user_input = int(input("Enter an integer value: "))
 except:
 # Bad value, 
  print("Error")
 continue
else:
 print("Valid input")

