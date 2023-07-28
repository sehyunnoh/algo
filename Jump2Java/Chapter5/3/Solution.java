class Calculator {
  boolean isOdd(int val) {
    return val % 2 == 1;
  }
}



public class Solution {
  public static void main(String[] args) {
    Calculator cal = new Calculator();
    System.out.println(cal.isOdd(3));  // 3은 홀수이므로 true 출력
    System.out.println(cal.isOdd(4)); 
  }  
}
