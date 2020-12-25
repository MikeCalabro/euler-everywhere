# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

def diagSpiralAdder(grid_size):
  spirals = (grid_size-1)/2
  diag_sum = 0
  number_gap = 2
  number_to_add = 1
  for _ in range(spirals):
    for _ in range(4):
      diag_sum += number_to_add
      number_to_add += number_gap
    number_gap += 2

  return diag_sum + number_to_add

def main():
  print(diagSpiralAdder(1001))

if __name__ == "__main__":
    main()
