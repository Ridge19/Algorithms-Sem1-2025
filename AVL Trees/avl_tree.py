from bst import *


class AVLTree(BST):
    """
    AVL tree implementation.  Extends BST class, overriding insertions.
    """

    def __init__(self):
         super().__init__()

    def insert(self, key):
        """
        Add key to tree.

        @param key Key to add to tree.

        """
        self.root = self.insert_from_root(self.root, key)

    def insert_from_root(self, root, key):
        """
        Recursive method to add key to tree.  Will perform necessary rotations to rebalance tree after insertion.
        
        @param root Root node of tree to add 'key'.
        @param key Key to add to tree.
        @return Update root node.
        """
        # check if root is empty
        if root is None:
            root = Node(key)
        elif key < root.key:
            # insert into left subtree
            root.left_child = self.insert_from_root(root.left_child, key)

            # check balance factor
            if self.balance_factor(root) >= 2:
                if key < root.left_child.key:
                    root = self.right_rotation(root)
                else:
                    root = self.left_right_rotation(root)
        elif key > root.key:
            # insert into right subtree
            root.right_child = self.insert_from_root(root.right_child, key)

            # check balance factor
            if self.balance_factor(root) <= -2:
                if key > root.right_child.key:
                    root = self.left_rotation(root)
                else:
                    root = self.right_left_rotation(root)
        else:
            # duplicate value, we do not insert into tree
            pass
        return root

    def balance_factor(self, node):
        """
        * Compute the balance factor.
        * 
        * @param node Node we like to compute balance factor for.
        * @return Balance factor of node.
        """
        return self.height_from_root(node.left_child) - self.height_from_root(node.right_child)

    def right_rotation(self, root):
        """
        * Perform right rotation between root and its leftChild.
        * 
        * @param root Root of tree to perform rotations on.
        * @return new root of rotation tree.
        """
        # TO BE IMPLEMENTED
        # Place holder
        child = root.left_child
        root.left_child = child.right_child
        child.right_child = root
        return child

    def left_rotation(self, root):
        """
        * Perform left rotation between root and its right child.
        * 
        * @param root Root of tree to perform rotation on.
        * @return new root of rotation tree.
        """
        child = root.right_child
        root.right_child = child.left_child
        child.left_child = root

        return child

    def left_right_rotation(self, root):
        """
        * Perform left-right rotation.
        * 
        * @param root Root of tree to perform rotations on.
        * @return new root of rotation tree.
        """
        # TO BE IMPLEMENTED
        # Place holder
        root.left_child = self.left_rotation(root.left_child)
        return self.right_rotation(root)

    def right_left_rotation(self, root):
        """
        * Perform right-left rotation.
        * 
        * @param root Root of tree to perform rotations on.
        * @return new root of rotation tree.
        """
        root.right_child = self.right_rotation(root.right_child)

        return self.left_rotation(root)
