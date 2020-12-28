
def isPandigital(num):
  strNum = str(num)
  if len(strNum) == len(set(strNum)):
    if '0' not in set(strNum):
      for i in range(1,len(strNum) +1):
        if str(i) not in set(strNum):
          return False
      return True
  return False

def isPrime(num):
  if num < 2:
    return False
  elif num ==2:
    return True
  else:
    return sum([i for i in range(1, int(num**0.5) + 1) if num % i == 0]) == 1

for i in range(10000000):
  if isPandigital(i) and isPrime(i):
    print(i)

