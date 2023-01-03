Script: my_if_b.py
By: CF
Purpose:If elif else to print outcome
Prerequisites: 
Tested: on Python v3.10.7 under Windows 11
Revision History:
Notes:
Do not edit the values in this script, all fixed settings are maintained at .\settings\Budget.py
This script has no error handling, by design.
'''
a = False
b = False
c = False
if a:
 print("a was true")
elif b:
 print("b was false")
elif c:
 print("c was true")
#prints a c as true
else:
 print("None of our boolean variables were true")
