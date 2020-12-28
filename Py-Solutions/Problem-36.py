# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

def decToBinary(num):
    if num == 1:
        return "1"
    stringNum = ""
    while num > 1:
        if num % 2 == 1:
            stringNum = "1" + stringNum
        else:
            stringNum = "0" + stringNum
        num = num // 2
    stringNum = "1" + stringNum
    return stringNum

def isPalindrome(str_num):
  rev_num = str_num[-1]
  for i in range(len(str_num)-2, -1, -1):
    rev_num += str_num[i]
  if rev_num == str_num:
    return True
  return False

def twoBasePal(limit):
    final_sum = 0
    for i in range(1,limit):
        if isPalindrome(str(i)) and isPalindrome(decToBinary(i)):
            final_sum += i
    return final_sum

def main():
    print(twoBasePal(1000000))

if __name__ == "__main__":
    main()
