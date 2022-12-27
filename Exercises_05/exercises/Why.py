'''
Script: why.py
By: CF
Purpose: Less than
Prerequisites: 
Tested: on Python v3.10.7 under Windows 11
Revision History:
Notes:
Do not edit the values in this script, all fixed settings are maintained at .\settings\Budget.py
This script has no error handling, by design.
'''
def find_num(number_list: list, number: int)->bool:
 for iterate_number in number_list:
  if iterate_number == number:
   return True
 else:
  pass
# change the value from 9 to 1 as it is less than
result = find_num([1,2,3,4,5,6,7,8], 1)
print(result)
#result is now true

