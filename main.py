# lp3thw p.142

s = (1, 'a', 3, 4)

for i in s:
  print('i =', i)


print("=" * 10)

def f(y):
  return y * 10

for j in map(f, s):
  print("j =", j)


print("=" * 10)

for k in map(lambda x: x*10, s):
  print("k =", k)
