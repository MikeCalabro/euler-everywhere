#include <stdio.h>

int threeOrFive(int limit);

int main() {
  int answer = threeOrFive(1000);
  printf("%d\n", answer);
  return 0;
}

int threeOrFive(int limit) {
  int sum = 0;
  for(int i = 1; i < limit; i++){
    if(i % 3 == 0 | i % 5 == 0){
      sum = sum + i;
    }
  }
  return sum;
}