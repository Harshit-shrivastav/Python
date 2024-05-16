i = str(input())
rev = ''
for c in i:
  rev = c + rev
if i == rev:
  print('PALINDROME')
else:
  print('NOT PALINDROME')
  