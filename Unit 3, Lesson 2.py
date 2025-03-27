num_items = int(input("How many items are you entering? "))
items = []
print("Enter your items now:")
for i in range (num_items):
  item = input(f"Next item: ")
  items.append(item)
print(f"\nYou have entered {num_items} items. ")
for item in items:
  print(item)
