def factorial(n):
  if n == 0 or n == 1:
    return 1
  result = 1
  for i in range (2, n + 1):
    result *= i
  return result
n = int(input("Enter a value for the upper limit, n: "))
for i in range(n + 1):
  print(f"{i}! = {factorial(i)}")
