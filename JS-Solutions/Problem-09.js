// There exists exactly one Pythagorean triplet for which a + b + c = 1000.
// Find the product abc.

const pythagSum = (sum) => {
  for (let a=1;a<sum/2;a++) {
    for (let b=1;b<sum/2;b++) {
      let c = Math.sqrt(a**2 + b**2)
      if (c % 1 == 0 & a + b + c == sum) {
        return [a,b,c];
      }
    }
  }
}

let triplet = pythagSum(1000);
let product = triplet[0] * triplet[1] * triplet[2];

console.log(triplet);
console.log(product);
