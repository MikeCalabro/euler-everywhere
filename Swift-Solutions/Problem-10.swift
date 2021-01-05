// Find the sum of all the primes below two million.
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

func sumOfPrimes(limit: Int) -> Int {
  var sum: Int = 2
  var i: Int = 3
  while i < limit {
    if isPrime(num: i) {
      sum += i
    }
    i += 2
  }
  return sum
}

print(sumOfPrimes(limit: 2000000))
