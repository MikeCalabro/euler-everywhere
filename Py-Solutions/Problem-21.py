# Evaluate the sum of all the amicable numbers under 10000.
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

amicableSum = 0
for i in range(2,10000):
  if(i == divisorSum(divisorSum(i)) and i != divisorSum(i)):
    print([i, divisorSum(i)])
    amicableSum += i

print(amicableSum)

