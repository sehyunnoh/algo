const Dictionary = require('./dictionary');

const phoneBook = new Dictionary();
phoneBook.add('Raymond', '123');
phoneBook.add('David', '345');
phoneBook.add('Cynthia', '456');
phoneBook.showAll();
console.log(phoneBook.find('David'));
phoneBook.remove('David');
phoneBook.showAll();
console.log(phoneBook.count());
phoneBook.clear();
console.log(phoneBook.count());
