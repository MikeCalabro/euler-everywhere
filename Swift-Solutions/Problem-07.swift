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
  var primeList: [Int] = []
  var i: Int = 2
  while primeList.count < n {
    if isPrime(num: i) {
      primeList.append(i)
    }
    i += 1
  }
  return primeList[primeList.count - 1]
}

print(nthPrime(n: 10_001))
