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
