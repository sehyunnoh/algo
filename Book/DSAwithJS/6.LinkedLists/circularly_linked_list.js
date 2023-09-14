const LinkedList = require('./linked_list.js');

class CircularlyLinkedList extends LinkedList {
  constructor() {
    super();
    this.head.next = this.head;
  }

  // Display all nodes in the linked list
  display() {
    let currNode = this.head;
    while (currNode.next !== this.head) {
      currNode = currNode.next;
      console.log(currNode.data)
    }
  }
}

module.exports = CircularlyLinkedList;