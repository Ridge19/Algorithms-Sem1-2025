import sys
from huffman_coding import *

def print_usage(prog_name):
    print(f"USAGE: {prog_name} [input string to encode]")


def main():
    args = sys.argv[1:]
    prog_name = "HuffmanCodingDemo"
    # not enough arguments
    if (len(args) != 1):
        print_usage(prog_name)
        exit(1)

    # input string
    input_string = args[0]

    print(f"Input String is: {input_string}")

    # build tree
    coding = HuffmanCoding()
    root = coding.build_tree(input_string)

    # assign codewords
    code_map = coding.assign_codeword(root)

    # print out the codeword map
    print("Applying Huffman coding, the following map is obtained:")
    for key, value in code_map.items():
        print(f"{key} -> {value}")

    # print out original string and same string encoded with the generated
    # Huffman code
    print("Original string encoded with this prefix code is:")
    input_char_seq = list(input_string)
    buffer = [code_map[char] for char in input_char_seq if char is not None]

    print("".join(buffer))

    # Calculate and print original and compressed sizes
    original_bytes, compressed_bytes = coding.calculate_sizes(input_string, code_map)
    print(f"Original size: {original_bytes} bytes")
    print(f"Compressed size: {compressed_bytes} bytes")

if __name__ == "__main__":
    main()