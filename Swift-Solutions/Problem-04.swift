import Foundation

func isPalindrome(num: Int) -> Bool {
  if String(num) == String(String(num).reversed()) {
    return true
  }
  return false
}

func maxPalindromeProduct(limit: Int) -> Int {
  var maxPalindrome: Int = 0
  for a in Int(round(Double(limit)/2))...limit-1 {
    for b in Int(round(Double(limit)/2))...limit-1 {
      if isPalindrome(num: a*b) && a*b > maxPalindrome {
        maxPalindrome = a*b
      }
    }
  }
  return maxPalindrome
}

print(maxPalindromeProduct(limit: 1000))
