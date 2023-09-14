class Node {
  constructor(data, next = null) {
    this.data = data;
    this.next = next;
  }
}

class LinkedList {
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

  // Find the previous node of the node containing the data
  findPrevious(data) {
    let currNode = this.head;
    while (currNode.next !== null && currNode.next.data !== data) {
      currNode = currNode.next;
    }
    return currNode;
  }

  // Remove the node containing the data
  remove(data) {
    const prevNode = this.findPrevious(data);
    if (prevNode.next !== null) {
      prevNode.next = prevNode.next.next;
    }
  }
}

module.exports = LinkedList;