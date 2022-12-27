'''
Script:mylib.cube.py
By: CF
Purpose: calculate
Prerequisites: 
Tested: on Python v3.10.7 under Windows 11
Revision History:
Notes:
Do not edit the values in this script, all fixed settings are maintained at .\settings\Budget.py
This script has no error handling, by design.
'''cube_text = "Yo, time to cube stuff!"
def cube(x):
 return x*x*x
if (__name__ == '__name__'):
 print(f"This module is called {__name__} and executes as a standalone script")
else:
 print(f"This module is called {__name__} and is being called by another script")
