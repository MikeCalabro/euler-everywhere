# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

def isPrime(num):
  if num < 2:
    return False
  elif num ==2:
    return True
  else:
    return sum([i for i in range(1, int(num**0.5) + 1) if num % i == 0]) == 1

def truncLeft(num):
  strNum = str(num)
  while len(strNum) >= 1:
    if not isPrime(int(strNum)):
      return False
    strNum = strNum[:-1]
  return True

def truncRight(num):
  strNum = str(num)
  while len(strNum) >= 1:
    if not isPrime(int(strNum)):
      return False
    strNum = strNum[1:]
  return True

checkList = [i for i in range(10,1000000) if isPrime(i)]

total = 0
for i in checkList:
  if truncLeft(i) and truncRight(i):
    print(i)
    total += i

print(total)
