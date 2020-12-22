# What is the largest prime factor of the number 600851475143?

isPrime <- function(num){
  for(i in (1:sqrt(num)+2)){
    if(num %% i == 0){
      return(FALSE);
    }
  }
  return(TRUE);
}

largestPrimeFactor <- function(num){
  largest <- 0
  for(i in (1:sqrt(num)+2)){
    if(num %% i == 0 && isPrime(i)){
      largest <- i
    }
  }
  return(largest);
}

print(largestPrimeFactor(600851475143))