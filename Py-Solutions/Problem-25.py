# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

def fibDigitFinder(length):
  fib_arr = [1,1,2]
  num_len = 1
  while num_len < length:
    next_up = fib_arr[-1] + fib_arr[-2]
    fib_arr.append(next_up)
    num_len = len(str(next_up))
  return len(fib_arr)

def main():
  print(fibDigitFinder(1000))

if __name__ == "__main__":
    main()