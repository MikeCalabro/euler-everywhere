// Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
import Foundation

func squareOfSum(limit: Int) -> Int {
  var sum: Int = 0
  for i in 1...limit {
    sum += i
  }
  return Int(pow(Double(sum),2))
}

func sumOfSquares(limit: Int) -> Int {
  var sum: Double = 0
  for i in 1...limit {
    sum += pow(Double(i),2)
  }
  return Int(sum)
}

func squareMinusSum(limit: Int) -> Int {
  return squareOfSum(limit: limit) - sumOfSquares(limit: limit)
}

print(squareMinusSum(limit: 100))
