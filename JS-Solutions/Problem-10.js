// Find the sum of all primes below 2 million

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

const sumOfPrimes = (limit) => {
  total = 0;
  for (let i=2;i<limit;i++) {
    if (isPrime(i)) {
      total += i;
    }
  }
  return total;
}

console.log(sumOfPrimes(2000000));
