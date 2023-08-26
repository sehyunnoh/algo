class Node {
  constructor(data) {
    this.data = data;
    this.prev = null;
    this.next = null;
  }
}

class DoublyLinkedList {
  constructor() {
    this.head = new Node("head");
  }

  // Find the node with the given data
  find(data) {
    let currNode = this.head;
    while (currNode.data !== data) {
      currNode = currNode.next;
      // if (currNode === null) {
      //   break
      // }
    }
    return currNode;
  }

  // Insert a new node after the node containing the data
  insert(newData, data) {
    const newNode = new Node(newData);
    const currNode = this.find(data);
    newNode.next = currNode.next;
    newNode.prev = currNode;
    currNode.next = newNode;
  }

  // Display all nodes in the linked list
  display() {
    let currNode = this.head;
    while (currNode.next !== null) {
      currNode = currNode.next;
      console.log(currNode.data)
    }
  }

  // Remove the node containing the data
  remove(data) {
    const currNode = this.find(data);
    if (currNode.next !== null) {
      currNode.prev.next = currNode.next;
      currNode.next.prev = currNode.prev;
      currNode.next = null;
      currNode.prev = null;
    }
  }

  // Find the last node
  findLast() {
    let currNode = this.head;
    while (currNode.next !== null) {
      currNode = currNode.next;
    }
    return currNode;
  }

  // Display all nodes in the linked list in reverse order
  dispReverse() {
    let currNode = this.findLast();
    while (currNode.prev !== null) {
      console.log(currNode.data);
      currNode = currNode.prev;
    }
  }
}

module.exports = DoublyLinkedList;