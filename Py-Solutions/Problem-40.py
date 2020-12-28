
num = 1
strNum = "0"
while len(strNum) < 1000010:
  strNum += str(num)
  num += 1

total = 1
for i in range(7):
  total *= int(strNum[10**i])

print(total)
