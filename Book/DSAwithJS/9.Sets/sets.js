class Set {
  constructor() {
    this.dataStore = [];
  }

  // add new element to the set
  add(data) {
    if (this.dataStore.indexOf(data) < 0) {
      this.dataStore.push(data);
      return true;
    }
    return false;
  }

  // remove element from the set
  remove(data) {
    let pos = this.dataStore.indexOf(data);
    if (pos > -1) {
      this.dataStore.splice(pos, 1);
      return true;
    } else {
      return false;
    }
  }

  // show all elements of the set
  show() {
    return this.dataStore;
  }

  // contains element in the set
  contains(data) {
    if (this.dataStore.indexOf(data) > -1) {
      return true;
    } else {
      return false;
    }
  }

  // union of two sets
  union(set) {
    let tempSet = new Set();
    for (let i=0; i<this.dataStore.length; i++) {
      tempSet.add(this.dataStore[i]);
    }
    for (let i=0; i <set.dataStore.length; i++) {
      if(!tempSet.contains(set.dataStore[i])){
        tempSet.dataStore.push(set.dataStore[i])
      }
    }
    return tempSet;
  }

  // intersection of two sets
  intersect(set) {
    let tempSet = new Set();
    for(let i=0; i < this.dataStore.length; i++) {
      if(set.contains(this.dataStore[i])) {
        tempSet.add(this.dataStore[i]);
      }
    }
    return tempSet;
  }

  // subset 
  subset(set) {
    if (this.size() > set.size()) {
      return false;
    } else {
      for ( let member of this.dataStore) {
        if (!set.contains(member)) {
          return false;
        }
      }
    }
    return true;
  }

  // size of the set
  size() {
    return this.dataStore.length;
  }

  // difference of two sets
  difference(set) {
    let tempSet = new Set();
    for (let i=0; i<this.dataStore.length; i++) {
      if (!set.contains(this.dataStore[i])){
        tempSet.add(this.dataStore[i]);
      }
    }
    return tempSet;
  }
}

module.exports = Set;