import math

# Welcome message
print("Welcome to the Even and Odd Detector!")

# Explain what the program does
print("This program determines if the product of two whole positive numbers is even or odd.")

# Get user input
number1 = int(input("Please enter your first number: ")) # First number input
number2 = int(input("Please enter your second number: ")) # Second number input

# Calculate product
product = number1 * number2

# Determine and display if the product is even or odd
if product % 2 == 0:
 print(f"The product of {number1} × {number2} is an even number.")
else:
 print(f"The product of {number1} × {number2} is an odd number.")

# Cube's inner diagonal calculation
print("\nNow, let's calculate the inner diagonal of a cube.")

# Get edge length input
edge_length = float(input("Please enter the edge length of your cube: "))

# Calculate inner diagonal using the square root function
inner_diagonal = edge_length * math.sqrt(3)

# Display the result with formatting
print(f"The length of the inner diagonal of a cube with side length {edge_length} is {inner_diagonal:.2f}")

# Coin change breakdown
print("\nChange Breakdown Calculator")

# Get the amount in cents
cents = int(input("Enter the amount of cents: "))

# Calculate number of quarters, dimes, nickels, and pennies
quarters = cents // 25
cents %= 25 # Remaining cents after quarters

dimes = cents // 10
cents %= 10 # Remaining cents after dimes

nickels = cents // 5
pennies = cents % 5 # Remaining cents after nickels

# Display the breakdown only if the number is greater than zero
if quarters > 0:
 print(f"{quarters} quarter(s)")
if dimes > 0:
 print(f"{dimes} dime(s)")
if nickels > 0:
 print(f"{nickels} nickel(s)")
if pennies > 0:
 print(f"{pennies} penny(ies)")
