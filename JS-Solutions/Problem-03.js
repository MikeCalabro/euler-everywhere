// What is the largest prime factor of the number 600851475143?

const isPrime = (num) => {
  if (num < 2) {
    return false;
  }
  if (num == 2) {
    return true;
  }
  for(let i=2;i<=Math.sqrt(num)+1;i++){
    if(num % i == 0){
      return(false);
    }
  }
  return(true);
}

const largestPrimeFactor = (num) => {
  let largest = 0;
  for(let i=2;i<=Math.sqrt(num)+2;i++){
    if(num % i == 0 & isPrime(i)){
      largest = i;
    }
  }
  return(largest);
}


console.log(largestPrimeFactor(600851475143));
