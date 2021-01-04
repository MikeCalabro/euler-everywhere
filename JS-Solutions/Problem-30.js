// Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

const PowerDigitSum = (num, power) => {
let numStr = String(num);
let sum = 0;
for (let i in numStr) {
  sum += parseInt(numStr[i])**power;
}
return sum;
}


let answer = 0;
for (let i=10;i<1000000;i++) {
  if (i == PowerDigitSum(i,5)) {
    console.log(i);
    answer += i;
  }
}

console.log(answer);
