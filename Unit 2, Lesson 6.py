print(f"{'N' :>3} {'SQR' :>7} {'Cubes' :>10} {'Roots' :>7}")

for N in range (10, 201, 15):
  square = N ** 2
  cube = N ** 3
  root = round(N ** 0.5, 2)
print(f"{N:>3} {square:>7} {cube:>10} {root:>7.2}")
