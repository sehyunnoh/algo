import java.util.*;

class Calculator {
  int avg(int[] data) {
    int sum = 0;
    for (int i=0; i < data.length; i++) {
      sum += data[i];
    }
    return sum / data.length;
  }

  int avg(ArrayList<Integer> data) {
    int sum = 0;
    for (int i=0; i < data.size(); i++) {
      sum += data.get(i);
    }
    return sum / data.size();
  }
}


public class Solution {
  public static void main(String[] args) {

    int[] data = {1, 3, 5, 7, 9};
    Calculator cal = new Calculator();
    int result = cal.avg(data);
    System.out.println(result);  // 5 출력
    
    ArrayList<Integer> data2 = new ArrayList<>(Arrays.asList(1, 3, 5, 7, 9));
    Calculator cal2 = new Calculator();
    int result2 = cal2.avg(data2);
    System.out.println(result2);  // 5 출력
  }
}
