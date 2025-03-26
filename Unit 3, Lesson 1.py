progname = "Lorem ipsum dolor sit amet, consectetur adipscing elit. Duis in"
for c in progname:
  print(c, sep=' ', end=' ')
print()
for c in range(len(progname)):
  print(c, progname[c])
  space_count = 0
  for c in progname:
    if c == ' ':
      space_count +=1
print(f"There are {space_count} spaces in the text.")
