class Stack {
  constructor() {
    this.dataStore = [];
    this.top = 0;
  }

  // push: adding an element to a stack
  push(element) {
    this.dataStore[this.top++] = element;
  }

  // pop: removing an element from a stack
  pop() {
    return this.dataStore[--this.top];
  }

  // peek: previewing an element from a stack
  peek() {
    return this.dataStore[this.top - 1];
  }

  // length: determining the number of elements in a stack
  length() {
    return this.top;
  }

  // clear: removing all elements from a stack
  clear() {
    this.top = 0;
  }
}

let s = new Stack();
s.push("David");
s.push("Raymond");
s.push("Bryan");
console.log("length: " + s.length()); // 3
console.log(s.peek());

let popped = s.pop();
console.log("The popped element is: " + popped); // Bryan
console.log(s.peek());

s.push("Cynthia");
console.log(s.peek());

s.clear();
console.log(s.length());

console.log(s.peek());
s.push("Clayton");
console.log(s.peek());
