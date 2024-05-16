i = int(input())
n = abs(i)
s = str(n)
rev = ''
for c in s:
  rev = c + rev
if i>0:
  print(rev)
else:
  print(f'-{rev}')