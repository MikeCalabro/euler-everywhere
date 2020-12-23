# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
import decimal
import math

decimal.getcontext().prec = 2000

max_j = 0
max_i = 0

for i in range(1,1000):
  string = str(decimal.Decimal(1)/decimal.Decimal(i) * 1000000000000000000000 % 1)[2:]
  test_str = str(decimal.Decimal(1)/decimal.Decimal(i) * 1000000000000000000000 % 1)[2:30]
  for j in range(1,len(string)-25):
    if test_str == string[j:j+28]:
      if j > max_j:
        max_j = j
        max_i = i
      break

def main():
  print(max_i, max_j)

if __name__ == "__main__":
    main()
