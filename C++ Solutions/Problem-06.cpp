/* # Find the difference between the sum of the squares of the first 100 natural numbers and the square of the sum. */

#include <iostream>
using namespace std;

int sumOfSquares(int limit);
int squareOfSums(int limit);
int squareMinusSum(int limit);

int main() {
  int answer = squareMinusSum(100);
  cout << answer << "\n";
  return 0;
}

int sumOfSquares(int limit) {
  int sum = 0;
  for (int i=1; i<=limit; i++) {
    sum += (i*i);
  }
  return sum;
}

int squareOfSums(int limit) {
  int sum = 0;
  for (int i=1; i<=limit; i++) {
    sum += i;
  }
  int square = sum * sum;
  return square;
}

int squareMinusSum(int limit) {
  int difference = squareOfSums(limit) - sumOfSquares(limit);
  return difference;
}
