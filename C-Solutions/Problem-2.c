/*
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
*/
#include <stdio.h>



int main(){
  int sum = 0;
  int arrLen = 32;
  int arr[32] = {1, 2};
  for(int i = 2; i < arrLen; i++) {
    arr[i] = arr[i-1] + arr[i-2];
  }
  for(int i = 0; i < arrLen; i++) {
    if(arr[i] % 2 == 0) {
      sum += arr[i];
    }
  }
  printf("%d\n", sum);
  return 0;
}