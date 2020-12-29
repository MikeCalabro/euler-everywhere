// What is the 10 001st prime number?

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

const nthPrime = (limit) => {
  let prime_list = [];
  let num = 2;
  while (prime_list.length < limit) {
    if (isPrime(num)) {
      prime_list.push(num);
    }
    num += 1;
  }
  return prime_list[prime_list.length - 1];
}

console.log(nthPrime(10001))
