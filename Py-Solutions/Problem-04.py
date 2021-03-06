# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(num):
  str_num = str(num)
  rev_num = str_num[-1]
  for i in range(len(str_num)-2, -1, -1):
    rev_num += str_num[i]
  if rev_num == str_num:
    return True
  return False

def largestPalindrome(limit):
  max = [0,0,0]
  for i in range(limit):
    for j in range(limit):
      if isPalindrome(i * j) and i * j > max[0]:
        max = [i*j,i,j]
  return(max)

def main():
  print(largestPalindrome(1000)[0])

if __name__ == "__main__":
    main()
