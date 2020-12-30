// What is the sum of the digits of the number 2**1000

const twoPowerArrayMaker = (power) => {
  digits = [1];
  for (let i=1;i<=power;i++){
    for (let j=digits.length-1;j>=0;j--) {
      digits[j] *= 2;
      if (digits[j] > 9 & digits[j-1] == undefined) {
        digits.unshift(1);
        digits[j + 1] -= 10;
      }
      while (digits[j + 1] > 9) {
        digits[j + 1] -= 10;
        digits[j] += 1;
      }
    }
  }
  return digits;
}

twoPowerArray = twoPowerArrayMaker(1000);
final_sum = twoPowerArray.reduce((a,b) => a + b);

console.log(final_sum);
