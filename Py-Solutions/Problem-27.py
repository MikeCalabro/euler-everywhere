# Find the product of the coefficients a and b for the quadratic expression that produces
# the maximum number of primes for consecutive values of n starting with n=0
import math

def isPrime(num):
  return sum([i for i in range(1, int(math.sqrt(num)) + 1) if num % i == 0]) == 1

b_list = [i for i in range(2,1000) if isPrime(i)]
a_list = [i for i in range(-999,1000, 2)]

ab_list = []
for a in a_list:
  for b in b_list:
    ab_list.append([a,b])

n = 1
while(len(ab_list) > 1):
  for i in ab_list:
    if n**2 + n*i[0] + i[1] < 2: 
      ab_list.remove(i)
    elif not isPrime(n**2 + n*i[0] + i[1]):
      ab_list.remove(i)
  n += 1
  print(ab_list)
  print(n)
