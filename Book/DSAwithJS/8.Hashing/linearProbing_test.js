let HashTableLinearProbing = require('./linearProbing.js');

let hTable = new HashTableLinearProbing(137);
let someNames = ["David", "Jennifer", "Donnie", "Raymond", "Cynthia", "Mike", "Clayton", "Danny", "Jonathan"];
for (let i=0; i<someNames.length; i++) {
  hTable.put(someNames[i], someNames[i]);
}

hTable.showDistro();
console.log(hTable.get("Jonathan"))
console.log(hTable.get("Mike"))