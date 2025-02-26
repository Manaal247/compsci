def make_changes(cents):
  quarters = cents // 25
  cents %=25
  
  dimes = cents // 10
  cents %=10
  
  nickels = cents // 5
  cents %=5
  
  pennies = cents  #Whatever is left are pennies
  
result = []
if quarters > 0:
  result.append(f"{quarters} quarter{'s' if quarters > 1 else ' '})
if dimes > 0:
  result.append(f"{dimes} dime{'s' if dimes > 1 else ' '})
  if nickels > 0:
  result.append(f"{nickels} nickel{'s' if nickels > 1 else ' '})
if pennies > 0:   
  result.append(f"{pennies} penn{'ies' if pennies > 1 else ' '})\

return ", " .join(result)
cents = int(input("Please enter the amount of change in cents"))
cents = cents % 100 #If more than $1, only keep the cents part
print(f"{cents} cents can be {make_change(cents)}.")
