// By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

func fibListMaker(limit: Int) -> Array<Int> {
  var fibList: [Int] = [1,2]
  while fibList[fibList.count - 1] + fibList[fibList.count - 2] <= limit {
    fibList.append(fibList[fibList.count - 1] + fibList[fibList.count - 2])
  }
  return fibList
}

func evenFibSummer(limit: Int) -> Int {
  var sum: Int = 0
  for i in fibListMaker(limit: limit) {
    if i % 2 == 0 {
      sum += i
    }
  }
  return sum
}

print(evenFibSummer(limit: 4000000))
