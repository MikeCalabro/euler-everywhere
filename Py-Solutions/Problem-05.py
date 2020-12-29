# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import math

def isPrime(num):
  return sum([i for i in range(1, int(math.sqrt(num)) + 1) if num % i == 0]) == 1

def isEvenlyDivisible(num, limit):
  for i in range(limit,int(math.floor(limit/2)),-1):
    if num % i != 0:
      return False
  return True

def smallestAllDivis(lim):
  start = 1
  for i in range(2,lim):
    if isPrime(i):
      start *= i
  while start % lim != 0:
    start -=1
  while True:
    if isEvenlyDivisible(start, lim):
      return(start)
    start += lim

def main():
  print(smallestAllDivis(20))

if __name__ == "__main__":
    main()
