/* Find the largest palindrome made from the product of two 3-digit numbers. */
#include <iostream>
#include <string>
using namespace std;

bool isPalindrome(int num);
int largestPalindromeProduct(int limit);

int main() {
  cout << largestPalindromeProduct(1000);
  return 0;
}

bool isPalindrome(int num) {
  string strNum = to_string(num);
  string reversed = "";
  for (int i=strNum.length()-1;i>=0;i--) {
    reversed += strNum[i];
  }
  if (strNum == reversed) {
    return true;
  }
  return false;
}

int largestPalindromeProduct(int limit) {
  int largest = 0;
  for (int a=limit/2;a<limit;a++) {
    for (int b=limit/2;b<limit;b++) {
      if ((isPalindrome(a*b)) & (a*b > largest)) {
        largest = a*b;
      }
    }
  }
  return largest;
}
