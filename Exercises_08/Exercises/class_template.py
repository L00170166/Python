'''
Script: class_template.py
By: CF
Purpose: Class and OO
Prerequisites: 
Tested: on Python v3.10.7 under Windows 11
Revision History:
Notes:
Do not edit the values in this script, all fixed settings are maintained at .\Python\Exercises_08\Exercises
This script has no error handling, by design.
'''
#Taken from earlier script of class
#name of class
class library:
#object name     
    name=""
    book=""
    date=""
    time=""
    dropoff=""
    condition=""
#Definition 
    def display(self):
        print("name : ",self.name)
        print("book : ",self.book)
        print("date : ",self.date)
        print("time : ",self.time)
        print("dropoff :",self.dropoff)
        print("condition :",self.condition)
# 
p1=library()
p1.name="Monty"
p1.book="bible"
p1.date="30 may 1966"
p1.time="15:30"
p1.drop="never"
p1.condition="burnt"
print()
p2=library()
p2.name="Cha"
p2.age="30"
p2.city="Limrick"
p2.eyes="green"
p2.height="4"
p1.display()
print()
#p1.display()


class lives:
    name=""
    house=""
    bedrooms=""
    cat=""
    dog=""
    cars=""
    bathrooms=""
    def display(self):
        print("name : ",self.name)
        print("house : ",self.house)
        print("bedrooms : ",self.bedrooms)
        print("cat : ",self.cat)
        print("dog : ",self.dog)
        print("cars : ",self.cars)
        print("bathrooms :",self.bathrooms)
p1=lives()
p1.cat="2"
p1.display()
p2=lives
p2.bedrooms="2"
p1.display()
print()