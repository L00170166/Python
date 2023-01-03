'''
Script: false.py
By: CF
Purpose: Is see if number can be divided calculate
Prerequisites: 
Tested: on Python v3.10.7 under Windows 11
Revision History:
Notes:
Do not edit the values in this script, all fixed settings are maintained at .\settings\Budget.py
This script has no error handling, by design.
'''
#to check if a number is divisible
def divisible(numerator: int, denominator: int)->bool:
#fraction divides the numerator
 return numerator % denominator == 0
#print the result
print(divisible(30,5))