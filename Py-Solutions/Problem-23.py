# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
import math

def divisorSum(num):
  sum_div = 1
  divs = []
  for i in range(2,1 + int(math.floor(math.sqrt(num)))):
    if(num % i == 0):
      sum_div += i
      divs.append(i)
  sum_div += sum([num/i for i in divs])
  if math.sqrt(num) % 1 == 0:
    sum_div -= int(math.sqrt(num))
  return sum_div

ab_list = set(i for i in range(1,28124) if divisorSum(i) > i)

def abundantsum(i):
  return any(i-a in ab_list for a in ab_list)

def main():
  print(sum([i for i in range(1,28124) if not abundantsum(i)]))

if __name__ == "__main__":
    main()
