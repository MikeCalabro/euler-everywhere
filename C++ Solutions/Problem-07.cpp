/* What is the 10 001st prime number? */

#include <iostream>
using namespace std;

bool isPrime(double num);
int nthPrime(int n);

int main()
{
  int n;
  cout << "Which Prime do yout want to know?\n";
  cin >> n;
  int answer = nthPrime(n);
  cout << "The " + to_string(n) + "th Prime is " + to_string(answer);
  return 0;
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

int nthPrime(int n) {
  int primes = 1;
  int counter = 1;
  while (primes < n) {
    counter += 2;
    primes += isPrime(counter);
  }
  return counter;
}