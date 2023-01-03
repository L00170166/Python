'''
Script:tuple1.py
By: CF
Purpose:Tuples print but also append code by adding items
Prerequisites:
Tested: on Python v3.10.7 under Windows 11
Revision History:
Notes:
Do not edit the values in this script, all fixed settings are maintained at .\settings\Budget.py
This script has no error handling, by design.
'''
my_tuple = ("four", "two", "three", "one", "four")
#how many times does "four" appear in the tuple
print (my_tuple.count ("four"))
# At what position in the tuple can i first find "two"
print(my_tuple.index("two"))