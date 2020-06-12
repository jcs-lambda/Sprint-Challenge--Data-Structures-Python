"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from queue import LifoQueue, Queue


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        elif value >= self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target < self.value:
            if self.left is not None:
                return self.left.contains(target)
        elif target > self.value:
            if self.right is not None:
                return self.right.contains(target)
        elif target == self.value:
            return True
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is not None:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)
        fn(self.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left is not None:
            node.in_order_print(node.left)
        print(node.value)
        if node.right is not None:
            node.in_order_print(node.right)
    
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.put(node)
        while not queue.empty():
            current_node = queue.get()
            print(current_node.value)
            if current_node.left is not None:
                queue.put(current_node.left)
            if current_node.right is not None:
                queue.put(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = LifoQueue()
        stack.put(node)
        while not stack.empty():
            current_node = stack.get()
            print(current_node.value)
            if current_node.right is not None:
                stack.put(current_node.right)
            if current_node.left is not None:
                stack.put(current_node.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left is not None:
            node.pre_order_dft(node.left)
        if node.right is not None:
            node.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left is not None:
            node.post_order_dft(node.left)
        if node.right is not None:
            node.post_order_dft(node.right)
        print(node.value)
