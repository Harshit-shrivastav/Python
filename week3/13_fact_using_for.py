# Factorial using for loop
result = 1
n = int(input("Enter a number: "))
if n < 0:
  print("Factorial does not exist for negative numbers")
else:
  for i in range(n, 0, -1):
    result = result*i
print(result)