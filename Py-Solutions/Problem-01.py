# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# Returns the sum of all numbers, up to a certain limit, divisible by 3 or 5
# The code inside the [brackets] creates the array, while sum() adds all the numbers in that array
def three_or_five(limit):
  return sum([i for i in range(limit) if i % 3 == 0 or i % 5 == 0])

def main():
  print(three_or_five(1000))
 
if __name__ == "__main__":
    main()
    