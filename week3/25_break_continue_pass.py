# Break is used to break the loop when a condition get satisfied
# Continue is used to skip the current iteration of the loop
# Pass is used to pass the current iteration of the loop
# Example of break
for i in range(1,11):
  if i == 5:
    break
  print(i)

# Example of continue
for i in range(1,11):
  if i == 5:
    continue
  print(i)

# Example of pass
for i in range(1,11):
  if i == 5:
    pass
  