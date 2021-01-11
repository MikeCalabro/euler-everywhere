/*
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
*/

#include <stdio.h>
#include <time.h>

int threeOrFive(int limit);


int main() {
  clock_t begin = clock();

  int answer = threeOrFive(1000);
  printf("%d\n", answer);
  
  clock_t end = clock();
  double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
  printf("RunTime: %f\n", time_spent);
  return 0;
}

int threeOrFive(int limit) {
  int sum = 0;
  for(int i=1; i<limit; i++){
    if(i % 3 == 0 | i % 5 == 0){
      sum = sum + i;
    }
  }
  return sum;
}