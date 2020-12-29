
def isPrime(num):
  if num < 2:
    return False
  elif num ==2:
    return True
  else:
    return sum([i for i in range(1, int(num**0.5) + 1) if num % i == 0]) == 1


for i in range(1000,9000):
  for j in range(1000,5000):
    if isPrime(i) and isPrime(i + j) and isPrime(i + j + j):
      if sorted([int(x) for x in str(i)]) == sorted([int(x) for x in str(i + j)]) and sorted([int(x) for x in str(i)]) == sorted([int(x) for x in str(i + j + j)]):
        print(i, i+j, i+j+j)
