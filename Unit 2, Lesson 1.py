x = input("Enter a number between 1 and 100:")
if x.isdigit():
  x = int(x)
  if 80 <= x <= 100:
    print("Grade: A")
  elif 70 <= x <= 79:
    print("Grade: B")
  elif 60 <= x <= 69:
    print("Grade: C")
  elif 50 <= x <= 59:
    print("Grade: D")
  elif 1 <= x <= 50:
    print("Grade: F")
  else:
    print("Invalid number. Please enter a number between 1 and 100.")
else: 
  print("Invalid input. Please enter a number")
