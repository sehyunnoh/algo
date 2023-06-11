package Study;

public class Solution {
  public static void main(String[] args) {
    int[] inputArray = {3, 6, -2, -5, 7, 3};
    System.out.println(solution(inputArray));
  }

  static int solution(int[] inputArray) {
    int maxProduct = 0;
    for (int i=0;i<inputArray.length; i++) {
        int product = inputArray[i] * inputArray[i+1];
            if (product > maxProduct) {
                maxProduct = product;
            } 
    }
    return maxProduct;
}
}