/* By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms. */
#include <stdio.h>

int main(){
  /* Initialize the limit (largest possible fib number) and sum (will eventually be our answer) */
  int limit = 4000000;
  int sum = 0;

  /* Populate the array of Fibonacci Numbers */
  int arr[50] = {1, 2};
  for(int i = 2; i < 50; i++) {
    arr[i] = arr[i-1] + arr[i-2];
    if(arr[i] + arr[i-1] > limit) {
      break;
    }
  }

  /* Calculate length of populated array (there are 0's on the end because I initialized with a number too big i.e 50) */ 
  int arrLen = sizeof(arr) / sizeof(arr[0]);

  /* Loop through the array, adding the even numbered terms to sum (which will be the final answer) */
  for(int i = 0; i < arrLen; i++) {
    if(arr[i] % 2 == 0) {
      sum += arr[i];
    }
  }

  /* Print the final answer */
  printf("%d\n", sum);
  return 0;
}
