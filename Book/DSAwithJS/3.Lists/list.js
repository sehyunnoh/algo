class List {
  constructor() {
    this.listSize = 0;
    this.pos = 0;
    this.dataStore = [];
  }

  // append: adding an element to a list
  append(element) {
    this.dataStore[this.listSize++] = element;
  }

  // find: finding an element in a list
  find(element) {
    for (let i = 0; i < this.dataStore.length; i++) {
      if (this.dataStore[i] == element) {
        return i;
      }
    }
    return -1;
  }

  // remove: removing an element from a list
  remove(element) {
    let foundAt = this.find(element);
    if (foundAt > -1) {
      this.dataStore.splice(foundAt, 1);
      --this.listSize;
      return true;
    }
    return false;
  }

  // length: determining the number of elements in a list
  length() {
    return this.listSize;
  }

  // toString: retrieving a list’s elements
  toString() {
    return this.dataStore;
  }

  // insert: inserting an element into a list
  insert(element, after) {
    let insertPos = this.find(after);
    if (insertPos > -1) {
      this.dataStore.splice(insertPos + 1, 0, element);
      ++this.listSize;
      return true;
    }
    return false;
  }
  
  // clear: removing all elements from a list
  clear() {
    delete this.dataStore;
    this.dataStore = [];
    this.listSize = this.pos = 0;
  }

  // contains: determining if a given value is in a list
  contains(element) {
    for (let i = 0; i < this.dataStore.length; i++) {
      if (this.dataStore[i] == element) {
        return true;
      }
    }
    return false;
  }

  // front: moving to the front of a list
  front() {
    this.pos = 0;
  }

  // end: moving to the end of a list
  end() {
    this.pos = this.listSize - 1;
  }

  // prev: moving to the previous element
  prev() {
    if (this.pos >= 0) {
      --this.pos;
    }
  }

  // next: moving to the next element
  next() {
    if (this.pos <= this.listSize - 1) {
      ++this.pos;
    }
  }

  // currPos: determining the current position in a list
  currPos() {
    return this.pos;
  }

  // moveTo: moving to a specific position in a list
  moveTo(position) {
    this.pos = position;
  }

  // getElement: retrieving an element at the current position
  getElement() {
    return this.dataStore[this.pos];
  }

}

class Customer {
  constructor(name, movie) {
    this.name = name;
    this.movie = movie;
  }
}

// test
console.log("====== test 1 ====== (append, remove, clear)");
let names = new List();
names.append('Cynthia');
names.append('Raymond');
names.append('Barbara');
console.log(names.toString());
names.remove('Raymond');
console.log(names.toString());
names.clear();
console.log(names.toString());

// // test 2
// console.log("====== test 2 ====== (front, end, prev, next, currPos, moveTo, getElement)");
// let names2 = new List();
// names2.append('Cynthia');
// names2.append('Raymond');
// names2.append('Barbara');
// names2.append('Jennifer');
// names2.append('Bryan');
// names2.append('Danny');
// names2.front();
// console.log(names2.getElement());
// names2.next();
// console.log(names2.getElement());
// names2.next();
// names2.next();
// names2.prev();
// console.log(names2.getElement());
// console.log(names2.currPos());
// names2.moveTo(3);
// console.log(names2.getElement());

// test 3
// console.log("====== test 3 ====== (iterate through a list)");
// let names3 = new List();
// names3.append('Cynthia');
// names3.append('Raymond');
// names3.append('Barbara');
// names3.append('Jennifer');
// names3.append('Bryan');
// names3.append('Danny');
// for (names3.front(); names3.currPos() < names3.length(); names3.next()) {
//   console.log(names3.getElement());
// }

// for (names3.end(); names3.currPos() >= 0; names3.prev()) {
//   console.log(names3.getElement());
// }

// function displayList(list) {
//   for (list.front(); list.currPos() < list.length(); list.next()) {
//     console.log(list.getElement());
//   }
// }

// function displayList(list) {
//   for (list.front(); list.currPos() < list.length(); list.next()) {
//     if (list.getElement() instanceof Customer) {
//       console.log(list.getElement()["name"] + ", " + list.getElement()["movie"]);
//     } else {
//       console.log(list.getElement());
//     }
//   }
// }

// function checkOut(name, movie, filmList, customerList) {
//   if (filmList.contains(movie)) {
//     let c = new Customer(name, movie);
//     customerList.append(c);
//     filmList.remove(movie);
//   } else {
//     console.log(movie + " is not available.");
//   }
// }


// // test 4
// console.log("====== test 4 ====== (read file)");
// let fs = require('fs');
// fs.readFile('./films.txt', 'utf8', function(err, data) {
//   if (err) {
//     return console.log(err);
//   }
//   let movies = data.split('\n');
  
//   let movieList = new List();
//   let customers = new List();
//   movies.forEach(item => {
//     movieList.append(item);
//   })

//   console.log("Available movies: \n");
//   displayList(movieList);

//   let name = "Jane Doe";
//   let movie = "The Godfather";

//   checkOut(name, movie, movieList, customers);

//   console.log("\n=== Customer Rentals: ===\n");
//   displayList(customers);

//   console.log("\n=== Movies Now Available ===\n");
//   displayList(movieList);

// });
