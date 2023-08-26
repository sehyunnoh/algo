const DoublyLinkedList = require("./doubly_linked_list")

let cities = new DoublyLinkedList();
cities.insert('Conway', 'head');
cities.insert('Russellville', 'Conway');
cities.insert('Carlisle', 'Russellville');
cities.insert("Alma", "Carlisle");
cities.display();
console.log();
cities.remove("Carlisle");
cities.display();
console.log();
cities.dispReverse();