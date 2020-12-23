# Find the sum of the digits in the number 100!
import math

def main():
  print(sum([int(i) for i in str(math.factorial(100))]))

if __name__ == '__main__':
    main()
