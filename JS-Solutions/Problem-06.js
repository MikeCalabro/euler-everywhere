// Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

const sumOfSquares = (limit) => {
  let sum = 0;
  for (let i=1;i<=limit;i++) {
    sum += i**2;
  }
  return sum;
}

const squareOfSum = (limit) => {
  let sum = 0;
  for (let i=1;i<=limit;i++) {
    sum += i;
  }
  return sum**2;
}

const squareMinusSum = (limit) => {
  return squareOfSum(limit) - sumOfSquares(limit);
}

console.log(squareMinusSum(100));
