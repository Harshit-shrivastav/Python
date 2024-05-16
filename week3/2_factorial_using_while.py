n = abs(int(input()))
s = str(n)
rev = ''
for c in range(s):
  rev = c + rev
if s>0:
  print(rev)
else:
  print(f'-{rev}')