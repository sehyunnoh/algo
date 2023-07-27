package Jump2Java.Chapter5;

class Animal {
  String name ;

  void setName(String name) {
    this.name = name;
  }
}

class Dog extends Animal {}




public class Inheritance {
  public static void main(String[] args) {
    Dog dog = new Dog();
    dog.setName("poppy");
    System.out.println(dog.name);
  }
}
