const PriorityQueue = require('./priority_queue.js');

class Patient {
  constructor(name, code) {
    this.name = name;
    this.code = code;
  }
}

let p = new Patient("Smith", 5);
let ed = new PriorityQueue();

ed.enqueue(p);
p = new Patient("Jones", 4);
ed.enqueue(p);
p = new Patient("Fehrenbach", 6)
ed.enqueue(p);
p = new Patient("Brown", 1);
ed.enqueue(p);
p = new Patient("Ingram", 1);
ed.enqueue(p);

console.log(ed.toString());

let seen = ed.dequeue();
console.log("Patient being treated: " + seen[0].name);
console.log("Patient waiting to be seen: ");
console.log(ed.toString());

// another round
seen = ed.dequeue();
console.log("Patient being treated: " + seen[0].name);
console.log("Patient waiting to be seen: ");
console.log(ed.toString());

seen = ed.dequeue();
console.log("Patient being treated: " + seen[0].name);


