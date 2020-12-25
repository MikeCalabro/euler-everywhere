# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
import math

total = 0
for i in range(3,1000000):
  fact_sum = 0
  for j in str(i):
    fact_sum += math.factorial(int(j))
  if fact_sum == i:
    print(i)
    total += i

print(total)
