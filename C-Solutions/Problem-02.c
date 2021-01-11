/* By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms. */
#include <stdio.h>
#include <time.h>

int evenFibSum(int limit);

int main(void) {
  clock_t begin = clock();

  int answer = evenFibSum(4000000);
  printf("%d\n", answer);

  clock_t end = clock();
  double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
  printf("RunTime: %f\n", time_spent);
  return 0;
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
