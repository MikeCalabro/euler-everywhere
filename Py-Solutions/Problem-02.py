# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def fib_maker(limit):
  fib_arr = [1,2]
  while fib_arr[-1] + fib_arr[-2] <= limit:
    fib_arr.append(fib_arr[-1] + fib_arr[-2])
  return fib_arr

def even_fib_summer(fib_list):
  return sum([i for i in fib_list if i % 2 == 0])

def main():
  print(even_fib_summer(fib_maker(4000000)))

if __name__ == "__main__":
    main()
    