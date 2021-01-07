// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import Foundation

func isPrime(_ num: Int) -> Bool {
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

func isFullyDivisible(num: Int, upTo limit: Int) -> Bool {
  for i in 2...limit {
    if num % i != 0 {
      return false
    }
  }
  return true
}

func smallestFullDivisor(of num: Int) -> Int {
  var counter: Int = 1
  for i in 1...num {
    if isPrime(i) {
      counter *= i
    }
  }
  counter *= num
  while !isFullyDivisible(num: counter, upTo: num) {
    counter += num
  }
  return counter
}

print(smallestFullDivisor(of: 20))
