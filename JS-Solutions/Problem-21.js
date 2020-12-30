// Evaluate the sum of all the amicable numbers under 10000.

const sumDivisors = (num) => {
  let total = 1;
  for (let i=2;i<Math.round(num**0.5) + 1;i++) {
    if (num % i == 0) {
      total += i + (num / i);
    }
  }
  if (num**0.5 % 1 == 0 & num != 1) {
    total -= num**0.5;
  }
  return total
}

const amicableSum = (limit) => {
  let total = 0;
  for(let i=1;i<limit;i++) {
    if (i == sumDivisors(sumDivisors(i)) & i != sumDivisors(i)) {
      total += i;
    }
  }
  return total;
}

console.log(amicableSum(10000));
