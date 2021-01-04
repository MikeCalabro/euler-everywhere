// Find the sum of all the multiples of 3 or 5 below 1000.

func threeOrFive(limit: Int) -> Int {
  var sum = 0
  for i in 1...limit-1 {
    if i % 3 == 0 || i % 5 == 0 {
      sum += i
    }
  }
  return sum
}

print(threeOrFive(limit: 1000))
