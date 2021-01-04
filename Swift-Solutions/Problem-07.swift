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

func nthPrime(n: Int) -> Int {
  var primeCount: Int = 1
  var i: Int = 1
  while primeCount < n {
    i += 2
    if isPrime(num: i) {
      primeCount += 1
    }
  }
  return i
}

print(nthPrime(n: 10_001))
