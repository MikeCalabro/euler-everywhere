# Find the least number for which the proportion of bouncy numbers is exactly 99%.

def isBouncy(num):
  numArr = [int(i) for i in str(num)]
  sortedArr = sorted(numArr)
  if numArr == sortedArr or numArr == list(reversed(sortedArr)):
    return False
  return True

bouncies = 0
total = 1
while True:
  if isBouncy(total):
    bouncies += 1
  if bouncies / float(total) == 0.99:
    print(total)
    break
  total += 1

