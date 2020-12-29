// Find the largest palindrome made from the product of two 3-digit numbers.

const isPalindrome = (num) => {
  let strNum = String(num);
  let revNum = strNum.split("").reverse().join("");
  if (strNum == revNum) {
    return true;
  }
  return false;
}

const largestDrome = (limit) => {
  let maxDrome = 0;
  for (let i=1;i<limit;i++) {
    for (let j=1;j<limit;j++) {
      if (isPalindrome(i * j) & i * j > maxDrome) {
        maxDrome = i * j;
      }
    }
  }
  return maxDrome;
}

console.log(largestDrome(1000));
