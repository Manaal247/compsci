score = input("Enter a number between 1 and 100:")
if score.isdigit():
  score = int(score)
  if 80 <= score <= 100:
    print("Grade: A")
  elif 70 <= score <= 79:
    print("Grade: B")
  elif 60 <= score <= 69:
    print("Grade: C")
  elif 50 <= score <= 59:
    print("Grade: D")
  elif 1 <= score <= 50:
    print("Grade: F")
  else:
    print("Invalid number. Please enter a number between 1 and 100.")
else: 
  print("Invalid input. Please enter a number")
