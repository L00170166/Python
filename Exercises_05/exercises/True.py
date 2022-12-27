#to check if a number is divisible
def divisible(numerator: int, denominator: int)->bool:
#fraction divides the numerator
 return numerator % denominator == 0
#change 4 to 5 or 3 to print the result as true
print(divisible(30,5))