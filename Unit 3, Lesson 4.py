ar2 = [
  [3, 4, 1, 2, 6,],
  [9, 2, 3, 7, 5,],
  [4, 2, 1, 0, 3]
  ]
for row in ar2:
  for num in row:
    print(num, end=" ")
row_sums = [sum(row) for row in ar2]
print(row_sums)
