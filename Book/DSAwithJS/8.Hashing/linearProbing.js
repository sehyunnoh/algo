let HashTable = require('./hashing.js');

class HashTableLinearProbing extends HashTable {
  constructor(size) {
    super(size);
    this.values = [];
  }

  put(key, data) {
    let pos = this.betterHash(key);
    if (this.table[pos] == undefined) {
      this.table[pos] = key;
      this.values[pos] = data
    } else {
      while (this.table[pos] != undefined) {
        pos++;
      }
      this.table[pos] = key;
      this.values[pos] = data;
    }
  }

  get(key) {
    let pos = -1;
    pos = this.betterHash(key);
    if (pos > -1) {
      for (let i=pos; this.table[i] != undefined; i++) {
        if (this.table[i] == key) {
          return this.values[i];
        }
      }
    }
    return undefined;
  }
}

module.exports = HashTableLinearProbing;