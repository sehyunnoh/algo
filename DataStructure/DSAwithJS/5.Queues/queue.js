class Queue {
  constructor() {
    this.dataStore = [];
  }

  // enqueue: add an element to the end of the queue
  enqueue(element) {
    this.dataStore.push(element);
  }

  // dequeue: remove an element from the front of the queue
  dequeue() {
    return this.dataStore.shift();
  }

  // front: returns the first element of the queue
  front() {
    return this.dataStore[0];
  }

  // back: returns the last element of the queue
  back() {
    return this.dataStore[this.dataStore.length - 1];
  }

  // toString: display all the elements of the queue
  toString() {
    let str = '';
    for (let i = 0; i < this.dataStore.length; i++) {
      str += this.dataStore[i] + '\n';
    }
    return str;
  }

  // empty: check if the queue is empty
  empty() {
    return this.dataStore.length === 0;
  }
}

module.exports = Queue;
