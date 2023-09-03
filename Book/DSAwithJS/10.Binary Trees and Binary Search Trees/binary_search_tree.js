let Node = require('./node.js')

class BST extends Node {
  constructor() {
    super();
    this.root = null;
  }

  insert(data) {
    let n = new Node(data, null, null);
    if (this.root === null) {
      this.root = n;
    } else {
      let current = this.root;
      let parent;
      while (true) {
        parent = current;
        if (data < current.data) {
          current = current.left;
          if (current === null) {
            parent.left = n;
            break
          }
        } else {
          current = current.right;
          if (current === null) {
            parent.right = n;
            break;
          }
        }
      }
    }

  }

  getMin() {
    let current = this.root;
    while (current.left !== null) {
      current = current.left;
    }
    return current.data;
  }

  getMax() {
    let current = this.root;
    while (current.right !== null) {
      current = current.right;
    }
    return current.data;
  }

  // Find the minimum value node in a BST
  findMin(node) {
    while (node.left) {
      node = node.left;
    }
    return node;
  }

  find(data) {
    let current = this.root;
    while(current.data !== data) {
      if (data < current.data) {
        current = current.left;
      } else {
        current = current.right;
      }
      if (current == null) {
        return null;
      }
    }
    return current;
  }

  // Remove a value from the BST
  remove(data) {
    const removeNode = (node, data) => {
      if (!node) {
        return null;
      }
      
      if (data === node.data) {
        // Node to be removed found

        // Case 1: Node has no children
        if (!node.left && !node.right) {
          return null;
        }

        // Case 2: Node has one child
        if (!node.left) {
          return node.right;
        }
        if (!node.right) {
          return node.left;
        }

        // Case 3: Node has two children
        const minRight = this.findMin(node.right);
        node.data = minRight.data;
        node.right = removeNode(node.right, minRight.data);
        return node;
      } else if (data < node.data) {
        // Move to the left subtree
        node.left = removeNode(node.left, data);
        return node;
      } else {
        // Move to the right subtree
        node.right = removeNode(node.right, data);
        return node;
      }
    };

    this.root = removeNode(this.root, data);
  }

}

module.exports = BST;