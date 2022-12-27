'''
Script: false1.py
By: CF
Purpose: Is to calculate income
Prerequisites:To pass True number needs to be equal
Tested: on Python v3.10.7 under Windows 11
Revision History:
Notes:
Do not edit the values in this script, all fixed settings are maintained at .\settings\Budget.py
This script has no error handling, by design.
'''
#function should return integers
def find_num(number_list: list, number: int)->bool:
 for iterate_number in number_list:
#is equal  
  if iterate_number == number:
    return True
 else:
    pass
result = find_num([1,2,3,4,5,6,7,8], 4)
print(result)
