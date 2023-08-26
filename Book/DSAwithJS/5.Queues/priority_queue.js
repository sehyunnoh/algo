const Queue = require('./queue');

class PriorityQueue extends Queue {
  constructor() {
    super();
  }

  dequeue() {
    let priority = this.dataStore[0].code;
    let index = 0;
    for(let i=0; i < this.dataStore.length; i++) {
      if (this.dataStore[i].code < priority) {
        priority = this.dataStore[i].code;
        index = i;
      }
    }
    return this.dataStore.splice(index, 1)
  }

  toString() {
    let str = '';
    for (let i = 0; i < this.dataStore.length; i++) {
      str += this.dataStore[i].name + " code: " + this.dataStore[i].code + '\n';
    }
    return str;
  }
}

module.exports = PriorityQueue;