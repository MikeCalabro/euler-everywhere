# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

# Creates a list of Fibonacci numbers below a certain limit number
def fib_maker(limit):
  fib_arr = [1,2]
  while fib_arr[-1] + fib_arr[-2] <= limit:
    fib_arr.append(fib_arr[-1] + fib_arr[-2])
  return fib_arr

# Creates an array of all the even elements of the fib list made above and sums them up
def even_fib_summer(fib_list):
  return sum([i for i in fib_list if i % 2 == 0])

def main():
  print(even_fib_summer(fib_maker(4000000)))

if __name__ == "__main__":
    main()
    