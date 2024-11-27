# Learning Tree Reversal by Building a Binary Search Tree

class TreeNode:
    """
    A tree node represents a single node in a Binary 
    Search Tree(BST). To be used by the BinarySearchTree class.
    """

    def __init__(self, key):
        """
        A constructor/initializer method

        Attributes:
            :self:
                Represents the instance of the class being created
            :key:
                Value of the node
        """
        self.key = key
        # 'left' and 'right' attributes represents the left and right nodes
        self.left = None
        self.right = None

    def __str__(self):
        """
        A method to return the string representation of the Binary 
        Search Tree(BST)
        """
        # self.key is the attribute of the current node 
        # that stores the value associated with the node
        return str(self.key)

class BinarySearchTree:
    """
    A Binary Search Tree(BST) is a data structure in which
    each node has at most two children, with the left child
    containing values less than the parent node and the right
    child containing values greater than the parent node.
    This allows for efficient searching and sorting operations.
    """

    def __init__(self):
        """
        A constructor/initializer method

        Attributes:
            :self: 
                Represents the instance of the class being created
        """
        # 'root' attribute represents the root node
        self.root = None

    def _insert(self, node, key):
        """
        A helper function and would be used by the actual
        insert method later on. This method is recursive, meaning
        it calls to traverse the tree until the appropriate location
        for the new node is found. Encapsulates the implementation of
        the insertion logic.

        Attributes:
            :self: 
                Represents the instance of the class being created
            :node:
                Represents the current node being evaluated
            :key:
                Value of the node
        """
        # Checking if leaf node or an empty spot in the tree 
        # where the new node should be inserted
        if node is None:
            # Creating an instance with the provided key
            return TreeNode(key)

        # Checking for values smaller or greater than the key
        if key < node.key:
            # Placing the new node in the left subtree
            node.left = self._insert(node.left, key)
        elif key > node.key:
            # Placing the new node in the right subtree
            node.right = self._insert(node.right, key)

        # Returning the current node to update the tree structure
        # at the higher levels of the recursive call stack
        return node

    def insert(self, key):
        """
        A method to insert a new node into the Binary Search Tree(BST)
        by calling the _insert helper method.

        Attributes:
            :self: 
                Represents the instance of the class being created
            :key:
                Key value to insert into the binary search tree
        """
        # Calling the helper method to insert the new node
        # self.root is the starting point for the insertion process
        self.root = self._insert(self.root, key)

    def _search(self, node, key):
        """
        A helper function and would be used by the actual search
        method later on. Performs the actual recursive search within
        the search tree.

        Attributes:
            :self: 
                Represents the instance of the class being created
            :node:
                Represents the current node being evaluated
            :key:
                Value of the node
        """
        # Checking if search reached the end of the branch without 
        # finding the key or if the key is found in the current node
        if node is None or node.key == key:
            return node
        # Checking if target key is less than key of the current node
        if key < node.key:
            return self._search(node.left, key) # The search continues in the left subtree
        # If the target key is greater than the key of the current node
        return self._search(node.right, key) # The search continues in the right subtree

    def search(self, key):
        """
        A method to search for a key in the Binary Search Tree(BST)
        by calling the _search helper method. 

        Attributes:
            :self: 
                Represents the instance of the class being created
            :key:
                Key value to insert into the binary search tree
        """
        # Calling the helper method to search for the key
        return self._search(self.root, key)

    def _delete(self, node, key):
        """
        A helper function and would be used by the actual delete
        function later on.

        Attributes:
            :self: 
                Represents the instance of the class being created
            :node:
                Represents the current node being evaluated
            :key:
                Key value to insert into the binary search tree
        """
        # Checking if the node is empty
        if node is None:
            return node
        # Checking if the key is less or greater than the current node's key
        # Valid for nodes with either one or no child
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else: # Scenarios when they're only two children
            if node.left is None: # If the left child is empty
                return node.right
            elif node.right is None: # If the right child is empty
                return node.left

            # Choosing the successor node
            node.key = self._min_value(node.right)
            # Recursively deleting the node with the minimum value from the right subtree
            node.right = self._delete(node.right, node.key)

        return node

    def delete(self, key):
        """
        A method to delete a node from the Binary Search Tree(BST)
        by calling the _delete helper method.

        Attributes:
            :self: 
                Represents the instance of the class being created
            :key:
                Value the user wants to delete from the binary search tree
        """
        # Calling the helper method to delete the value
        self.root = self._delete(self.root, key)

    def _min_value(self, node):
        """
        A helper function to find the minimum value in a subtree
        
        Attributes:
            :self: 
                Represents the instance of the class being created
            :node:
                Represents the current node being evaluated
        """
        # Iterating through the left children of the given node
        # until the leftmost(smallest) leaf node in the subtree is found
        while node.left is not None:
            # Storing the leftmost node in the 'node' variable
            node = node.left 
        # Returning the key of the leftmost node
        return node.key

    def _inorder_traversal(self, node, result):
        """
        A helper function to traverse the tree based on the inorder
        traversal method. A depth-first binary tree traversal algorithm.
        Visits left subtree -> root -> right subtree

        Attributes:
            :self: 
                Represents the instance of the class being created
            :node:
                Represents the current node being considered during 
                the traversal
            :result:
                A list to which the keys of the nodes are appended in
                sorted order
        """
        # Checking if the node is empty
        if node:
            # Exploring the left subtree in-order manner recursively
            self._inorder_traversal(node.left, result)
            # Appending the key of the current node to the result list
            result.append(node.key)
            # Exploring the right subtree in-order manner recursively
            self._inorder_traversal(node.right, result)

    def inorder_traversal(self):
        """
        A method for performing an inorder traversal of the Binary 
        Search Tree(BST). Calls the _inorder_traversal helper method.
        Returns the keys of the nodes in sorted order.

        Attributes:
            :self: 
                Represents the instance of the class being created
        """
        # Storing the keys of the nodes in sorted order
        result = []
        # Calling the helper method to perform the traversal
        self._inorder_traversal(self.root, result)

        # Returning the list of keys
        return result


if __name__ == "__main__":
    # Creating an instance of the BinarySearchTree class
    bst = BinarySearchTree()
    # Creating a list of nodes
    nodes = [2, 89, 50, 30, 20, 40, 70, 4, 67, 100, 60, 80, 500]
    # Inserting the nodes into the binary search tree
    for node in nodes:
        bst.insert(node)

    # Searching for a key in the binary search tree
    print('Search for 80:', bst.search(80)) # Should return 80

    # Conducting in-order traversal
    print('In-order traversal:', bst.inorder_traversal())

    # Deleting a key from the binary search tree
    bst.delete(67)

    # Searching for a deleted key in the binary search tree
    print('Search for 67:', bst.search(67)) # Should return None

    # Conducting in-order traversal again
    print('In-order traversal after deleting 67:', bst.inorder_traversal())
