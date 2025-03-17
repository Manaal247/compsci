print ("Welcome to the even and odd detector!")
print ("This program determines if the product of two whole positive numbers will be even or odd!")
number = int(input("Please enter your first number"))
numberr = int(input("Please enter your second number"))
product = number * numberr
if product % 2 == 0:
  print ("the product of (number) x (numberr) will be an even number")
else:
  print ("The product of (number) x (numberr) will be an odd number")

import math
print ("I will find the cube's inner diagonal for any edge length!")
edge_length = float(input("Please enter the edge length of your cube: "))
inner_diagonal = edge_length * math.sqrt(3)
print (f"The length of the inner diagonal of a cube with side length {edge_length} is: f{inner_diagonal: .2f}")

cents = int(input("Enter the amount of cents: "))
quarters = cents // 25
cents %=25
  
dimes = cents // 10
cents %=10
  
nickels = cents // 5
cents %=5
  
pennies = cents

print ("Change breakdown")
if quarters > 0:
  print(quarters, "quarter(s)")
if dimes > 0:
  print(dimes, "dime(s)")
if nickels > 0:
  print(nickels, "nickel(s)")
if pennies > 0:
  print(pennies, "pennies")
