n = int(input("Enter a number"))
print("\nTriangular Numbers:")
for i in range(1, n + 1):
  print(i, i * (i + 1) // 2)
print("\nFactorials: ")
f = 1
for i in range(1, n + 1):
  f *= i 
  print (i, f)
