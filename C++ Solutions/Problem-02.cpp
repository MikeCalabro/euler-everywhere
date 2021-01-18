/* 
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms. 
*/

#include <iostream>
using namespace std;

int evenFibSum(int limit);

int main(void) {
  int answer = evenFibSum(4000000);
  cout << answer << "\n";
}

int evenFibSum(int limit) {
  int last = 2, secondLast = 1, evenSum = 0, placeHolder;
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
