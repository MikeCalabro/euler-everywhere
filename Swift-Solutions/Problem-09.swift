// There exists exactly one Pythagorean triplet for which a + b + c = 1000.
// Find the product abc.

import Foundation

func tripletFinder(sum: Int) -> Array<Int> {
  for a in 1...Int(sum/2) {
    for b in 1...Int(sum/2) {
      let c: Double = pow(pow(Double(a),2) + pow(Double(b),2),0.5)
      if Double(a) + Double(b) + c == Double(sum) {
        return [a,b,Int(c)]
      }
    }
  }
  return [0,0,0]
}

let triplet: [Int] = tripletFinder(sum: 1000)
print(triplet[0]*triplet[1]*triplet[2])
