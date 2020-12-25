
def powerSum(power):
  total = 0
  for i in range(2,200000):
    count = 0
    for d in str(i):
      count += int(d)**power
    if count == i:
      total += count
  return total

def main():
  print(powerSum(5))

if __name__ == "__main__":
    main()
