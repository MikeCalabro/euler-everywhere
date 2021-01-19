# How many digit factorial chains, with a starting number below one million, contain exactly sixty non-repeating terms?
import math

def digFactSum(num):
  factSum = 0
  strNum = str(num)
  for i in strNum:
    factSum += math.factorial(int(i))
  return factSum

def nonRepeatingTerms(startNum):
  numList = [startNum]
  checkNum = digFactSum(startNum)
  while checkNum not in numList:
    numList.append(checkNum)
    checkNum = digFactSum(checkNum)
  return len(numList)

answer = sum([1 for i in range(1,1000000) if nonRepeatingTerms(i) == 60])
print(answer)
