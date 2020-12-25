# Looked at the forum for the template for this answer
# Modified it to my typical format

def isPrime(num):
  if num < 2:
    return False
  elif num ==2:
    return True
  else:
    return sum([i for i in range(1, int(num**0.5) + 1) if num % i == 0]) == 1

def prime_counter(a, b):
    n = 0
    while True:
        if not isPrime(n**2 + a*n + b):
          break
        n += 1
    return n

def maxPrimeFinder(limit):
  b_list = [i for i in range(2,limit) if isPrime(i)]
  a_list = range(-1*limit+1,limit,2)
  max_count = 0
  for a in a_list:
    for b in b_list:
      count = prime_counter(a,b)
      if count > max_count:
        max_a = a
        max_b = b
        max_count = count     
  return [max_a, max_b, max_a*max_b, max_count]

def main():
  print(maxPrimeFinder(1000))

if __name__ == "__main__":
    main()
