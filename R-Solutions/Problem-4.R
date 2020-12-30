# Find the largest palindrome made from the product of two 3-digit numbers.

isPalindrome <- function(num) {
  pal_arr <- c()
  x = 1
  while(num > 9) {
    pal_arr <- append(pal_arr, (num %% 10**x) / 10**(x-1))
    num <- num - num %% 10**x
    x <- x + 1
  }
  return(sum(pal_arr == rev(pal_arr)) == length(pal_arr))
}

largestPalindrome <- function(limit) {
  max_palindrome <- 0
  for (i in ((limit/2):limit)) {
    for (j in ((limit/2):limit)) {
      if (isPalindrome(i*j) && i*j > max_palindrome) {
        max_palindrome <- i*j
      }
    }
  }
  return(max_palindrome)
}

largestPalindrome(1000)
