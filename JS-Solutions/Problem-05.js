// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

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

const minPrimeProduct = (limit) => {
  let product = 1;
  for (i=2;i<=limit;i++) {
    if (isPrime(i)) {
      product *= i;
    }
  }
  return product;
}

const allDivisorsWork = (num, limit) => {
  for (let i=2; i<=limit; i++) {
    if (num % i != 0) {
      return false;
    }
  }
  return true;
}

const evenlyDivis = (limit) => {
  smallest = minPrimeProduct(limit);
  while (smallest % limit != 0) {
    smallest -= 1;
  }
  while(! allDivisorsWork(smallest, limit)) {
    smallest += limit;
  }
  return smallest;
}

console.log(evenlyDivis(20));
