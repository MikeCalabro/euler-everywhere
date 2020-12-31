# what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

def isPrime(num):
  if num < 2:
    return False
  elif num ==2:
    return True
  else:
    return sum([i for i in range(1, int(num**0.5) + 1) if num % i == 0]) == 1

def diagSpiralAdder(grid_size):
  spirals = (grid_size-1)/2
  total_nums = 0 
  total_primes = 0
  number_gap = 2
  number_to_add = 1
  for _ in range(spirals):
    for _ in range(4):
      number_to_add += number_gap
      total_nums += 1
      if isPrime(number_to_add):
        total_primes += 1
    number_gap += 2
  total_nums += 1
  print([total_primes,total_nums])
  return total_primes*10 < total_nums

count = 26591
while not diagSpiralAdder(count):
  print(diagSpiralAdder(count))
  count += 2

print(count)