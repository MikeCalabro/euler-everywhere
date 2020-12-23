# What is the value of the first triangle number to have over five hundred divisors?
import math

def numDivisors(num):
  divs = 0
  for i in range(1,1 + int(math.floor(math.sqrt(num)))):
    if(num % i == 0):
      divs += 1
  if math.sqrt(num) % 1 == 0:
    return divs * 2 - 1
  return divs * 2

def triDivisors(num_divisors):
  tri_num = 1
  adder = 2
  while numDivisors(tri_num) <= num_divisors:
    tri_num += adder
    adder += 1
  return [tri_num, numDivisors(tri_num)]

def main():
  print(triDivisors(500))

if __name__ == '__main__':
  main()
