/*
 What is the largest prime factor of the number 13195? 
 */

#include <iostream>
using namespace std;

bool isPrime(double num);
int largestPrimeFactor(double num);

int main(void) {
  int x = largestPrimeFactor(13195);
  cout << x << "\n";
}

bool isPrime(double num) {
  if (num <= 1) {
    return false;
  }
  if (num == 2) {
    return true;
  }
  for (int i=2;i<int(sqrt(num))+1;i++) {
    if (int(num) % i == 0) {
      return false;
    }
  }
  return true;
}

int largestPrimeFactor(double num) {
  int intNum = int(num);
  int largest = 0;
  for (int i=2;i<int(sqrt(num))+1;i++) {
    if ((intNum % i == 0) & (isPrime(i))) {
      largest = i;
    }
  }
  return largest;
}
