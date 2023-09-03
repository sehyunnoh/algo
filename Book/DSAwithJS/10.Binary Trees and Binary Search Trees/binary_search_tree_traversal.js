let BST = require('./binary_search_tree.js');

function inOrder(node) {
  if (node !== null) {
    inOrder(node.left);
    console.log(node.show());
    inOrder(node.right);
  }
}

function preOrder(node) {
  if (node !== null) {
    console.log(node.show());
    preOrder(node.left);
    preOrder(node.right);
  }
}

function postOrder(node) {
  if (node !== null) {
    postOrder(node.left);
    postOrder(node.right);
    console.log(node.show());
  }
}

let nums = new BST();
nums.insert(23);
nums.insert(45);
nums.insert(16);
nums.insert(37);
nums.insert(3);
nums.insert(99);
nums.insert(22);
console.log("InOrder traversal: ");
inOrder(nums.root);
console.log("PreOrder traversal: ");
preOrder(nums.root);
console.log("PostOrder traversal: ");
postOrder(nums.root);

nums.remove(16);
console.log("InOrder traversal: ");
inOrder(nums.root);