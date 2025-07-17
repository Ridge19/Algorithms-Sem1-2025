"""
Node for Huffman tree.
"""
class Node:
    def __init__(self, s, f, left, right):
        """
        * Constructor.
        *
        * @param s Symbol/character to assign to node.
        * @param f Frequency of symbol/character.
        * @param left Left child of this node (set to null if no left child)
        * @param right Right child of this node (set to null if no right child)        
        """
        self.symbol = s
        self.frequency = f
        self.left_child = left
        self.right_child = right

    """
     * Node compared based on frequency.
     *
     * @param other Other node we are comparing against.   
    """
    def __lt__(self, other):
        return self.frequency < other.frequency

    def __eq__(self, other):
        return self.frequency == other.frequency

    def __gt__(self, other):
        return self.frequency > other.frequency
