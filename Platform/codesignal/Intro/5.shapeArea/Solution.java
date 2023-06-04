public class Solution {
  public static void main(String[] args) {
    // System.out.println(new Solution().solution(3));
    System.out.println(solution(3));
  }

  static int solution(int n){
    int result = 1;
    for(int i=1; i<n; i++) {
      result += 4*i;
    }
    return result;
  }
}