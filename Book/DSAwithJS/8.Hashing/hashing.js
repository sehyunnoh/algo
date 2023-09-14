class HashTable {
  constructor(size) {
    this.table = new Array(size);
  }

  simpleHash(data) {
    let total = 0;
    for (let i = 0; i < data.length; i++) {
      total += data.charCodeAt(i);
    }
    return total % this.table.length;
  }

  // it is not working properly. and the logic is not clear.
  betterHash(data) {
    const H = 37;
    let total = 0;
    for (let i=0; i<data.length; i++) {
      total += H * total + data.charCodeAt(i);
    }
    total = total % this.table.length;
    if (total <= 0) {
      total += this.table.length-1;
    }
    return parseInt(total);
  }


  put(data) {
    // let pos = this.simpleHash(data);
    let pos = this.betterHash(data);
    this.table[pos] = data;
  }

  showDistro() {
    let n = 0;
    for (let i=0; i<this.table.length; i++) {
      if (this.table[i] !== undefined) {
        console.log(i + ": " + this.table[i]);
      }
    }
  }

  get(key) {
    return this.table[this.betterHash(key)]
  }
}

module.exports = HashTable;