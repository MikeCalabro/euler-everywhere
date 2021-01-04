# What is the 10,001st prime number?
import math

def isPrime(num):
  if num < 2:
    return False
  elif num ==2:
    return True
  else:
    return sum([i for i in range(1, int(num**0.5) + 1) if num % i == 0]) == 1

def primeFinder(n):
  counter = 1
  nth = 1
  while nth < n:
    counter += 2
    if isPrime(counter):
      nth += 1
  nth_prime = counter
  return nth_prime

def main():
  print(primeFinder(10001))

if __name__ == '__main__':
  main()
