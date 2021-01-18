/*
What is the value of the first triangle number to have over five hundred divisors?
*/

#include <iostream>
using namespace std;

int numDivisors(int num);
int triDivisors(int numDivs);

int main() {
  int answer = triDivisors(500);
  cout << answer << "\n";
  return 0;
}

int numDivisors(int num) {
  int divisors = 0;
  for (int i=1; i<int(sqrt(double(num)))+1; i++) {
    if (num % i == 0) {
      divisors += 2;
    }
  }
  return divisors;
}

int triDivisors(int numDivs) {
  int smallest = 1;
  int index = 1;
  while (numDivisors(smallest) < numDivs) {
    index += 1;
    smallest += index;
  }
  return smallest;
}
