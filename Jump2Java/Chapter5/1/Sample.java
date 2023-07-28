class Calculator {
  int value;

  Calculator() {
      this.value = 0;
  }

  void add(int val) {
      this.value += val;
  }

  int getValue() {
      return this.value;
  }
}

class UpgradeCalculator extends Calculator {
  int minus(int val) {
    this.value -= val;
    return this.value;
  }
}

public class Sample {
  public static void main(String[] args) {
      // Calculator cal = new Calculator();
      UpgradeCalculator cal = new UpgradeCalculator();
      cal.add(10);
      cal.minus(3);
      System.out.println(cal.getValue());  // 10 출력


  }
}