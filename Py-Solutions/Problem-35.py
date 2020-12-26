# How many circular primes are there below one million?

def isPrime(num):
  if num < 2:
    return False
  elif num ==2:
    return True
  else:
    return sum([i for i in range(1, int(num**0.5) + 1) if num % i == 0]) == 1

def isCircular (num):
  x = str(num)
  for _ in range(len(x)):
    if not isPrime(int(x)):
      return False
    last_letter = x[-1]
    x = x[:-1]
    x = last_letter + x
  return True

def main():
  prime_list = [i for i in range(1,1000000,2) if isPrime(i)]
  print(len([i for i in prime_list if isCircular(i)]) + 1)

if __name__ == "__main__":
    main()
