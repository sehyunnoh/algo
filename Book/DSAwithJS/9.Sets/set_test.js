let Set = require('./sets.js');

// let names = new Set();
// names.add('David');
// names.add('Jennifer');
// names.add('Cynthia');
// names.add('Mike');
// names.add('Raymond');
// if (names.add('Mike')) {
//   console.log("Mike added");
// } else {
//   console.log("Can't add Mike, must already be in set");
// }

// console.log(names.show());
// let removed = "Mike"
// if (names.remove(removed)) {
//   console.log(removed + " removed.");
// } else {
//   console.log(removed + " not removed.");
// }


// union test
// let cis = new Set();
// cis.add('Mike');
// cis.add('Clayton');
// cis.add('Jennifer');
// cis.add('Raymond');
// let dmp = new Set();
// dmp.add("Raymond");
// dmp.add("Cynthia");
// dmp.add("Jonathan");
// let it = new Set();
// it = cis.union(dmp);
// console.log(it.show())

// intersection test
// let cis = new Set();
// cis.add('Mike');
// cis.add('Clayton');
// cis.add('Jennifer');
// cis.add('Raymond');
// let dmp = new Set();
// dmp.add("Raymond");
// dmp.add("Cynthia");
// dmp.add("Bryan");
// let inter = cis.intersect(dmp);
// console.log(inter.show());

// subset test
// let it = new Set();
// it.add("Cynthia");
// it.add("Clayton");
// it.add("Jennifer");
// it.add("Danny");
// it.add("Jonathan");
// it.add("Terrill");
// it.add("Raymond");
// it.add("Mike");

// let dmp = new Set();
// dmp.add("Cynthia");
// dmp.add("Raymond");
// dmp.add("Jonathan");
// dmp.add("Shirley")
// if (dmp.subset(it)){
//   console.log("DMP is a subset of IT.");
// } else {
//   console.log("DMP is not a subset of IT.");
// }

// difference test
let cis = new Set();
let it = new Set();
cis.add("Clayton");
cis.add("Jennifer");
cis.add("Danny");
it.add("Bryan");
it.add("Clayton");
it.add("Jennifer")
let diff = new Set();
diff = cis.difference(it);
console.log(diff.show());