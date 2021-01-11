# A number chain is created by continuously adding the square of the digits 
# in a number to form a new number until it has been seen before.
# How many starting numbers below ten million will arrive at 89?

def digitSquare(num):
  return sum([int(i)**2 for i in str(num)])

def endsIn89(num):
  while True:
    if num == 1:
      return False
    if num == 89:
      return True
    num = digitSquare(num)

answer = sum([1 for i in range(1,10000000) if endsIn89(i)])

print(answer)
