'''
Script: project2.py
By: CF
Purpose: calls cube and square code in mylib folder. I have changed the values below. 
Prerequisites: 
Tested: on Python v3.10.7 under Windows 11
Revision History:
Notes:
Do not edit the values in this script, all fixed settings are maintained at .\settings\Budget.py
This script has no error handling, by design.
'''

import mylib.cube as mycube
import mylib.square as mysquare
print(mycube.cube_text, mycube.cube(5))
print(mysquare.square_text, mysquare.square(4))