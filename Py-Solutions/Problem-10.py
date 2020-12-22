# Find the sum of all the primes below two million.
import math

def isPrime(num):
  return sum([i for i in range(1, int(math.sqrt(num)) + 1) if num % i == 0]) == 1

def primeSum(limit):
  return sum([i for i in range(3,limit, 2) if isPrime(i)]) + 2

def main():
  print(primeSum(2000000))

if __name__ == '__main__':
  main()
