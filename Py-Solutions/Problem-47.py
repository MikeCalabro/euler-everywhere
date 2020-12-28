
def isPrime(num):
  if num < 2:
    return False
  elif num ==2:
    return True
  else:
    return sum([i for i in range(1, int(num**0.5) + 1) if num % i == 0]) == 1

primes = set(i for i in range(1000000) if isPrime(i))

def PrimeFactors(num):
  init = num
  prime_list = []
  while num > 1:
    for i in primes:
      if num % i == 0:
        prime_list.append(i)
        num = num / i
        break
  return [init, len(set(prime_list)),set(prime_list)]

for i in range(2000,1000000):
  if PrimeFactors(i)[1] == 4 and PrimeFactors(i+1)[1] == 4 and PrimeFactors(i+2)[1] == 4 and PrimeFactors(i+3)[1] == 4:
    print(PrimeFactors(i))

