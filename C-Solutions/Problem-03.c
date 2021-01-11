/* What is the largest prime factor of the number 600851475143? */

#include <stdio.h>
#include <time.h>

int main() {
  clock_t begin = clock();

  printf("Hello World!\n");
  
  clock_t end = clock();
  double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
  printf("RunTime: %f\n", time_spent);
  return 0;
}
