import java.util.Arrays;

public class Solution {
  public static void main(String[] args) {
    int[] arr = {6, 2, 3, 8};
    System.out.println(new Solution().solution(arr));   
  }

  int solution(int[] statues) {
    Arrays.sort(statues);
    return statues[statues.length - 1] - statues[0] - statues.length + 1;
  }
  
}
