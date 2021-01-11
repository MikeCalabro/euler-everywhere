/* What is the largest prime factor of the number 600851475143? */
#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool isPrime(int num);

int main() {
  int answer = isPrime(25);
  printf("%d\n", answer);
  return 0;
}

bool isPrime(int num) {
  int limit = num;
  return false;
}