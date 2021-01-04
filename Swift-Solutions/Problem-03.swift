// What is the largest prime factor of the number 600851475143 ?
import Foundation

func isPrime(num: Int) -> Bool {
  if num < 2 {
    return false
  }
  if num == 2 {
    return true
  }
  let limit: Int = Int(pow(Double(num),0.5))+1
  for i in 2...limit {
    if num % i == 0 {
      return false
    }
  }
  return true
}

func largestPrimeFactor(num: Int) -> Int {
  var maxPrimeFactor: Int = 0
  let limit: Int = Int(pow(Double(num),0.5))+1
  for i in 2...limit {
    if num % i == 0 && isPrime(num: i) {
      maxPrimeFactor = i
    }
  }
  return maxPrimeFactor
}

print(largestPrimeFactor(num: 600851475143))
