from bst import *


def print_help():
    print("Available commands:\n"
          + "    insert <key>\n"
          + "    search <key>\n"
          + "    min\n"
          + "    max\n"
          + "    height\n"
          + "    inorder\n"
          + "    preorder\n"
          + "    postorder\n"
          + "    print_ascii\n"
          + "    quit|end\n"
          )


def process_operations(tree):
    """
    Get next command/operation from stdin.
    """

    while True:
        command = input("").split()
        operation = command[0]
        if operation == "insert":
            key = int(command[1])
            tree.insert(key)
        elif operation == "search":
            key = int(command[1])
            if tree.search(key):
                print(f"Key {key} found.")
            else:
                print(f"Key {key} not found.")
        elif operation == 'min':
            min_key = tree.min()
            if min_key != BST.EMPTY_TREE:
                print(f"Min key = {min_key}")
            else:
                print("Tree is empty.")
        elif operation == 'max':
            max_key = tree.max()
            if max_key != BST.EMPTY_TREE:
                print(f"Max key = {max_key}")
            else:
                print(f"Tree is empty.")
        elif operation == "height":
            height = tree.height()
            print(f"Height = {height}")
        elif operation == "inorder":
            tree.inorder()
        elif operation == "preorder":
            tree.preorder()
        elif operation == "postorder":
            tree.postorder()
        elif operation == "print_ascii":
            tree.ascii_print()
        elif operation == "quit" or command == "end":
            break
        else:
            print(f"Did not recognize command {command}. Enter valid command.")
            print_help()


def main():
    tree = BST()
    process_operations(tree)


if __name__ == "__main__":
    main()
