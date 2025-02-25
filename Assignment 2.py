import math
print ("I will find the cube's inner diagonal for any edge length!")
edge_length = float(input("Please enter the edge length of your cube: "))
inner_diagonal = edge_length * math.sqrt(3)
print (f"The length of the inner diagonal of a cube with side length {edge_length} is: f{inner_diagonal: .2f}")
