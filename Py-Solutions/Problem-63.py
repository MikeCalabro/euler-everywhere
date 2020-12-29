# How many n-digit positive integers exist which are also an nth power?

total = 0
for i in range(1,100):
  num = 1
  while len(str(num**i)) <= i:
    if len(str(num**i)) == i:
      print(num, i, num**i)
      total += 1
    num += 1

print(total)
