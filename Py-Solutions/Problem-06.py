# Find the difference between the sum of the squares of the first 100 natural numbers and the square of the sum.


def squareMinusSum(limit):
  square_of_sum = (((1 + limit)*limit)/2)**2
  sum_of_square = sum([i**2 for i in range(1,limit + 1)])
  return square_of_sum - sum_of_square


def main():
  print(squareMinusSum(100))


if __name__ == '__main__':
  main()
