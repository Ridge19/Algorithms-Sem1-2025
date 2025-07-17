from avl_tree import *


def print_help():
    print("Available commands:\n"
          + "    insert <number>\n"
          + "    height\n"
          + "    print_ascii\n"
          + "    quit|end\n"
          )


def process_operations(tree):
    """
    Get next command/operation from stdin.
    """

    while True:
        command = input().split()
        if command[0] == "insert":
            key = int(command[1])
            tree.insert(key)
        elif command[0] == "height":
            height = tree.height()
            print(f"Height = {height}")
        elif command[0] == "print_ascii":
            tree.ascii_print()
        elif command[0] == "quit" or command[0] == "end":
            break
        else:
            print(f"Did not recognize command {command}. Enter valid command.")
            print_help()


def main():
    tree = AVLTree()
    process_operations(tree)


if __name__ == "__main__":
    main()
