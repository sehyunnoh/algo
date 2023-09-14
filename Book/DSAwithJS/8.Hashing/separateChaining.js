let HashTable = require('./hashing.js');

class HashTableSeparateChaining extends HashTable {
  constructor(size) {
    super(size);
  }

  buildChains() {
    for (let i=0; i<this.table.length; i++) {
      this.table[i] = new Array();;
    }
  }

  showDistro() {
    let n = 0;
    for (let i=0; i<this.table.length; i++) {
      if (this.table[i][0] !== undefined) {
        console.log(i + ": " + this.table[i]);
      }
    }
  }

  put(key, data) {
    let pos = this.betterHash(key);
    let index = 0;
    if (this.table[pos][index] == undefined){
      this.table[pos][index++] = data;
    } else {
      while (this.table[pos][index] != undefined) {
        index++;
      }
      this.table[pos][index] = data;
    }
  }
  
  get(key) {
    let index = 0;
    let pos = this.betterHash(key);
    if (this.table[pos][index] == key) {
      return this.table[pos][index];
    } else {
      let length = this.table[pos].length;
      while (this.table[pos][index] != key && index < length) {
        index++;
      }
      return this.table[pos][index]
    }
  }

}

module.exports = HashTableSeparateChaining;