/*
Which starting number, under one thousand, produces the longest Collatz chain?
*/

#include <iostream>
using namespace std;

int collatzLength(int num);
int longestCollatz(int limit);

int main() {
  int answer = longestCollatz(1000);
  cout << answer << "\n";
  return 0;
}

int collatzLength(int num) {
  int length = 1;
  while (num > 1) {
    if (num % 2 == 0) {
      num = num / 2;
    } else {
      num = (num*3) + 1;
    }
    length += 1;
  }
  return length;
}

int longestCollatz(int limit) {
  int longestNum = 0, longestChain = 0, i = 2;
  int testLength;
  while (i < limit) {
    testLength = collatzLength(i);
    if (testLength > longestChain) {
      longestNum = i;
      longestChain = testLength;
    }
    i += 1;
  }
  return longestNum;
}
