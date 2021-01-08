/* By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms. */
#include <iostream>
using namespace std;

int evenFibSum(int limit);

int main(void) {
  int answer = evenFibSum(4000000);
  cout << answer;
}

int evenFibSum(int limit) {
  int last = 2;
  int secondLast = 1;
  int placeHolder;
  int evenSum = 0;
  while (last < limit) {
    if (last % 2 == 0) {
      evenSum += last;
    }
    placeHolder = last;
    last = last + secondLast;
    secondLast = placeHolder;
  }
  return evenSum;
}
