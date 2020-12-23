# What is the largest prime factor of the number 600851475143?
import math

def isPrime(num):
  return sum([i for i in range(1, int(math.sqrt(num)) + 1) if num % i == 0]) == 1

def largestPrimeFactor(num):
  return [i for i in range(2, int(math.sqrt(num)) + 1) if num % i == 0 and isPrime(i)][-1]

print(largestPrimeFactor(600851475143))
