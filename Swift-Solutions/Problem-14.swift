// Which starting number, under one million, produces the longest Collatz chain?

func collatzLength(of num: Int) -> Int {
  var length: Int = 1
  var tracker: Int = num
  while tracker > 1 {
    if tracker % 2 == 0 {
      tracker = tracker / 2
    } else {
      tracker = tracker * 3 + 1
    }
    length += 1
  }
  return length
}

func longestChain(under limit: Int) -> Int {
  var longest: Int = 0
  for n in 1..<limit {
    if collatzLength(of: n) > collatzLength(of: longest) {
      longest = n
    }
  }
  return longest
}

print(longestChain(under: 1000000))
