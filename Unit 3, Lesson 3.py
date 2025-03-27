items = ["Apples", "Bananas", "Cherries", "Dosa"]
sizes = [ ]
for i in range(len(items)):
  size = len(items[i])
  sizes.append(size)
for i in range(len(sizes)):
  print(f"{sizes[i]} {items[i]}")
