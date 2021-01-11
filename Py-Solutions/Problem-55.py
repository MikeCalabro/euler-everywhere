# How many Lychrel numbers are there below ten-thousand?
def isPalindrome(num):
  if str(num) == reverse(str(num)):
    return True
  return False

def reverse(strNum):
  rev_num = strNum[-1]
  for i in range(len(strNum)-2, -1, -1):
    rev_num += strNum[i]
  return rev_num

def isLychrel(num):
  iteration = 0
  while iteration < 50:
    num += int(reverse(str(num)))
    if isPalindrome(num):
      return False
    iteration += 1
  return True

total = sum([1 for i in range(1,10000) if isLychrel(i)])

print(total)
