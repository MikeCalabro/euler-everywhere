// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import Foundation

var counter: Int = 2*3*5*7*11*13*17*19*20
func isFullyDivisible(num: Int, upTo limit: Int) -> Bool {
  for i in 2...limit {
    if num % i != 0 {
      return false
    }
  }
  return true
}

while !isFullyDivisible(num: counter, upTo: 20) {
  counter += 20
}

print(counter)
