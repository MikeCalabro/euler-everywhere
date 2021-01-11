/* Find the sum of all the multiples of 3 or 5 below 1000. */

public class Problem01 {
  public static void main(String[] args) {
    int answer = threeOrFive(1000);
    System.out.println(answer);
  }
  public static int threeOrFive(int limit) {
    int sum = 0;
    for (int i=0;i<limit;i++) {
      if (i % 3 == 0 | i % 5 == 0) {
        sum += i;
      }
    }
    return sum;
  }
}
