
def isPrime(num):
  if num < 2:
    return False
  elif num ==2:
    return True
  else:
    return sum([i for i in range(1, int(num**0.5) + 1) if num % i == 0]) == 1

dubSquares = set(2*i**2 for i in range(0,10000))
primes = set(i for i in range(1,10000) if isPrime(i))

def isBach(num):
  return any(num - a in primes for a in dubSquares)

for i in range(3,10000,2):
  if not isBach(i):
    print(i)
    break
