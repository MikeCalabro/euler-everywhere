// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
// Find the sum of all the multiples of 3 or 5 below 1000.

const three_or_five = (limit) => {
  answer = 0;
  for(i=3;i<limit;i++){
    if(i % 3 == 0 | i % 5 == 0){
      answer += i;
    }
  }
  return(answer);
}

console.log(three_or_five(1000));