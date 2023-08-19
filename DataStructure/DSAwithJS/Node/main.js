// main.js
// To use the 'import' keyword, we need to use the 'type' attribute in the package.json file.
// { "type": "module" }
const Person = require('./person'); // Import the Person class from the person.js file

const person1 = new Person('Alice', 30);
person1.greet();

const person2 = new Person('Bob', 25);
person2.greet();
