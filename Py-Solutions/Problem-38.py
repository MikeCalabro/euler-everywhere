
for num in range(9,9876):
  strNum = str(num)
  mult = 2
  while len(strNum) < 9:
    strNum += str(num*mult)
    mult += 1
  if len(strNum) == 9:
      if len(strNum) == len(set(strNum)):
        if '0' not in set(strNum):
          print(num, strNum)

