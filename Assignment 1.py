print ("Welcome to the even and odd detector!")
print ("This program determines if the product of two whole positive numbers will be even or odd!")
number = int(input("Please enter your first number"))
numberr = int(input("Please enter your second number"))
product = number * numberr
if product % 2 == 0:
  print (f"the product of (number) x (numberr) will be an even number")
else:
  print (f"The product of (number) x (numberr) will be an odd number")
