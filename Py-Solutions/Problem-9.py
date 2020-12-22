# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
import math

def pythagoreanProduct(sum):
  for a in range(1,500):
    for b in range(1,500):
      c = math.sqrt(a**2 + b**2)
      if c % 1 == 0 and a + b + int(c) == sum:
        return(int(a*b*c))

def main():
  print(pythagoreanProduct(1000))

if __name__ == '__main__':
  main()
  