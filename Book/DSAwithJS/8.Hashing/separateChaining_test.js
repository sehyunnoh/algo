let HashTableSeparateChaining = require('./separateChaining.js');

let hTable = new HashTableSeparateChaining(137);
hTable.buildChains();
let someNames = ["David", "Jennifer", "Donnie", "Raymond", "Cynthia", "Mike", "Clayton", "Danny", "Jonathan"];
for (let i=0; i < someNames.length; i++) {
  hTable.put(someNames[i], someNames[i]);
}
hTable.showDistro();
console.log(hTable.get("Jonathan"))