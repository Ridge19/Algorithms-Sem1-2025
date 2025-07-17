from queue import PriorityQueue
from node import Node


class HuffmanCoding:
    """
    Implements Huffman coding: building the tree and assigning codewords.
    """

    ASCII_SIZE = 256

    def build_tree(self, inputString):
        """
        Build the Huffman tree from inputString.
        Returns the root node of the constructed Huffman tree.
        """
        # Count frequencies
        freq = [0] * HuffmanCoding.ASCII_SIZE
        for ch in inputString:
            freq[ord(ch)] += 1

        # Build priority queue of leaf nodes
        pq = PriorityQueue()
        for i in range(HuffmanCoding.ASCII_SIZE):
            if freq[i] > 0:
                pq.put((freq[i], Node(chr(i), freq[i], None, None)))

        # Build the tree
        while pq.qsize() > 1:
            left = pq.get()[1]
            right = pq.get()[1]
            merged = Node(None, left.frequency + right.frequency, left, right)
            pq.put((merged.frequency, merged))

        if not pq.empty():
            return pq.get()[1]
        return None

    def assign_codeword(self, root):
        """
        Assign codewords to the leaf nodes/symbols.
        Returns a map of each symbol/character to the assigned codeword.
        """
        code_map = {}
        self.recursive_assign_codeword(code_map, root, "")
        return code_map

    def recursive_assign_codeword(self, code_map, curr, curr_code_str):
        """
        Recursive implementation to assign the codewords.
        """
        if curr is None:
            return
        # Leaf node: assign codeword
        if curr.left_child is None and curr.right_child is None:
            if curr.symbol is not None:
                code_map[curr.symbol] = curr_code_str
            return
        # Traverse left and right
        self.recursive_assign_codeword(code_map, curr.left_child, curr_code_str + "0")
        self.recursive_assign_codeword(code_map, curr.right_child, curr_code_str + "1")

    def calculate_sizes(self, inputString, code_map):
        """
        Calculates the byte size before and after compression.
        Returns (original_size_bytes, compressed_size_bytes)
        """
        # Original size: 8 bits per character
        original_bits = len(inputString) * 8
        original_bytes = (original_bits + 7) // 8

        # Compressed size: sum of codeword lengths * frequency
        compressed_bits = 0
        freq = {}
        for ch in inputString:
            freq[ch] = freq.get(ch, 0) + 1
        for ch in freq:
            compressed_bits += freq[ch] * len(code_map[ch])
        compressed_bytes = (compressed_bits + 7) // 8

        return original_bytes, compressed_bytes
