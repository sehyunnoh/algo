let HashTable = require('./hashing.js');

let someNames = ["David", "Jennifer", "Donnie", "Raymond", "Cynthia", "Mike", "Clayton", "Danny", "Jonathan"];

let hTable = new HashTable(137);
for (let i=0; i<someNames.length; i++) {
  hTable.put(someNames[i]);
}
hTable.showDistro();