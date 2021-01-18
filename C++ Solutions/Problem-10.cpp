/* 
Find the sum of all the primes below two million. 
*/

#include <iostream>
using namespace std;

bool isPrime(double num);
int primeSum(int limit);

int main()
{
  int limit;
  cout << "Find the sum of all primes below ...\n";
  cin >> limit;
  int answer = primeSum(limit);
  cout << answer;
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

int primeSum(int limit) {
  int sum = 2;
  for (int i=3; i<limit; i+=2) {
    if (isPrime(i)) {
      sum += i;
    }
  }
  return sum;
}
