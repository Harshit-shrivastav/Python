import random

l = []
for i in range(1000000):
  l.append(random.randint(1,10000000))


# l = [2000, 22001, 2002, 2003, 2004]
print(l)
i = 0
n = 0
while (n != -1):
  print("Enter a number to search:")
  n = int(input())
  flag = 0
  for i in range(len(l)):
    if n == l[i]:
      print("Element found")
      flag = 1
      break
  if flag == 0:
    print("Element not found")

