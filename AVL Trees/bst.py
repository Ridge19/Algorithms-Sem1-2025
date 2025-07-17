import ascii_printer
import math


class BST:
    EMPTY_TREE = -1

    def __init__(self):
        self.root = None

    def insert(self, key):
        """
        Add key to tree.
        
        @param key
        """
        self.root = self.insert_from_root(self.root, key)

    def insert_from_root(self, root, key):
        """
        Recursive method to add key to tree.
        
        @param root Root node of tree to add 'key'.
        @param key Key to add to tree.
        @return Update root node.   
        """
        # check if root is empty
        if root is None:
            root = Node(key)
        elif key < root.key:
            root.left_child = self.insert_from_root(root.left_child, key)
        elif key > root.key:
            root.right_child = self.insert_from_root(root.right_child, key)
        else:
            # duplicate value, we do not insert into tree
            pass

        return root

    def search(self, key):
        """
        Add key to tree.
        
        @param key key to search for.
        @return True if key is in the BST, otherwise false.
        """
        return self.search_from_root(self.root, key)

    def search_from_root(self, root, key):
        """
        Recursive method to search for key in tree.
        
        @param root Root node of tree to search 'key'.
        @param key Key to search for.
        @return True if key is found, otherwise false.
        """
        # check if root is empty
        # if so, either root of whole tree is empty, or we reach an empty node,
        # meaning we have not found the key in the tree
        if root is None:
            return False
        elif key < root.key:
            return self.search_from_root(root.left_child, key)
        elif key > root.key:
            return self.search_from_root(root.right_child, key)
        else:
            pass

        # key must be equal to root.key
        return True

    def inorder(self):
        """
        Inorder traversal of tree.
        """
        self.inorder_from_root(self.root)
        print("")

    def inorder_from_root(self, root):
        if root is None:
            return

        self.inorder_from_root(root.left_child)
        print(f"{root.key} ", end="")
        self.inorder_from_root(root.right_child)

    def preorder(self):
        """
        preorder traversal of tree
        """
        self.preorder_from_root(self.root)
        print("")

    def preorder_from_root(self, root):
        """
        Preorder traversal of tree.
        
        @param root Root node of the tree.
        """
        if root is None:
            return

        print(f"{root.key} ", end="")
        self.preorder_from_root(root.left_child)
        self.preorder_from_root(root.right_child)

    def postorder(self):
        """
        Postorder traversal of tree.
        """
        self.postorder_from_root(self.root)
        print("")

    def postorder_from_root(self, root):
        """
        Postorder traversal of tree.
        
        @param root Root node of the tree.
        """
        if root is None:
            return

        self.postorder_from_root(root.left_child)
        self.postorder_from_root(root.right_child)
        # In general, might be better to use a function object here, but for this lab, we just print to stdout
        print(f"{root.key} ", end="")

    def ascii_print(self):
        """
        Print out tree in ascii text.
        """
        ascii_printer.print_node(self.root)

    def min(self):
        """
        Find minimum key in tree.

        @return Minimum key in tree.
        """
        min_node = self.min_from_root(self.root);
        if min_node is not None:
            return min_node.key
        # empty tree
        else:
            return BST.EMPTY_TREE

    def min_from_root(self, root):
        """
        Recursive method for finding 
        @param root Root node of tree
        @return Minimum key in tree.
        """
        if root.left_child is None:
            return root

        return self.min_from_root(root.left_child)

    def max(self):
        """
        Find maximum key in tree.
        @return Maximum key in tree.
        """
        max_node = self.max_from_root(self.root)
        if (max_node != None):
            return max_node.key
        else:
            return BST.EMPTY_TREE

    def max_from_root(self, root):
        """
        Recursive method for finding maximum key in tree.
        @param root Root node of tree.
        @return Maximum key in tree.
        """
        if root.right_child is None:
            return root

        return self.max_from_root(root.right_child)

    def height(self):
        """
        Compute the height of the tree.
        @return Height of tree.
        """
        return self.height_from_root(self.root)

    def height_from_root(self, root):
        """
        Recursive method for computing the height of tree.
        
        @param root Root node of tree.
        
        @return Height of tree.       
        """
        if root is None:
            return -1

        return 1 + max(self.height_from_root(root.left_child),
                       self.height_from_root(root.right_child))


class Node:
    def __init__(self, key):
        """
        Constructor

        @param key Key to store in node.
        """
        # For this lab, we only store ints, but in general we can store any object/type that is Comparable. */
        self.key = key
        # Reference to left child. */
        self.left_child = None
        # Reference to right child. */
        self.right_child = None

    def key(self):
        """
        @return Key stored in node.
        """
        return self.key

    def left_child(self):
        """
        @return Reference to left child of node.
        """
        return self.left_child

    def right_child(self):
        """
        @return Reference to right child of node
        """
        return self.right_child
