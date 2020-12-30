// What is the value of the first triangle number to have over five hundred divisors?

const triMaker = (len) => {
  let num = 0;
  let adder = 1;
  while (adder <= len) {
    num += adder;
    adder += 1;
  }
  return num
}

const numDivisors = (num) => {
  let total = 1;
  for (let i=2;i<Math.round(num**0.5) + 1;i++) {
    if (num % i == 0) {
      total += 1;
    }
  }
  total *= 2;
  if (num**0.5 % 1 == 0) {
    total -= 1;
  }
  return total
}

const longDivisorList = (len) => {
  let max_divisors = 0;
  let n = 1;
  let tri_num, divs;
  while (max_divisors <= len) {
    tri_num = triMaker(n);
    divs = numDivisors(tri_num);
    if (divs > max_divisors) {
      max_divisors = divs;
    }
    n += 1;
  }
  return [tri_num, divs];
}

console.log(longDivisorList(500));
