# Which starting number, under one million, produces the longest Collatz chain?

def longestCollatz(limit):
  max_len = 0
  max_starter = 0
  for n in range(3,limit):
    starter = n
    chain_len = 1
    while n > 1:
      if n % 2 == 0:
        n = n/2
      else:
        n = 3*n+1
      chain_len += 1
    if chain_len > max_len:
      max_starter = starter
      max_len = chain_len
  return([max_starter, max_len])

def main():
  print(longestCollatz(1000000))

if __name__ == '__main__':
  main()
