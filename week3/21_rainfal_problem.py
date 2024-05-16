#day = int(input())
day = int(input('Please enter a day'))
for i in range(day, day+1):
  rainfal = 0
  n = 0
  while(n != -1):
    rainfal += n
    n = int(input('Please enter rainfall:'))
  print(f'Total rainfall is {rainfal}')

    