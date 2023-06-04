public class Solution {
  public static void main(String[] args) {
    int[] arr = {3, 6, -2, -5, 7, 3};
    System.out.println(new Solution().solution(arr));
  }
  
  int solution(int[] inputArray) {
    int max = Integer.MIN_VALUE;
    for (int i = 0; i < inputArray.length - 1; i++) {
      int product = inputArray[i] * inputArray[i + 1];
      if (product > max) {
        max = product;
      }
    }
    return max;
  }
}
