class Node {
  constructor(data, left, right) {
    this.data = data;
    this.count = 1;
    this.left = left;
    this.right = right;
  }

  show() {
    return this.data;
  }
}

module.exports = Node;