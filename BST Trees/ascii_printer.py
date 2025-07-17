import math


# Java code to print out binary tree in ASCII.
#
# Code obtained from: http://stackoverflow.com/questions/4965335/how-to-print-binary-tree-diagram
# Author: michal.kreuzman on Stackoverflow
# Modified: Jeffrey Chan, 2016, Lei Yang, 2021


def print_node(root):
    """
    Print out tree rooted at 'root'.
    """
    max_level = get_max_level(root)

    print_node_internal([root], 1, max_level)


def print_node_internal(nodes, level, max_level):
    """
    Print out internals of tree.
    """
    if nodes == [] or is_all_elements_null(nodes):
        return

    floor = max_level - level
    end_lines = int(math.pow(2, (max(floor - 1, 0))))
    first_spaces = int(math.pow(2, floor) - 1)
    between_spaces = int(math.pow(2, (floor + 1)) - 1)

    print_with_white_spaces(first_spaces)

    new_nodes = []
    for node in nodes:
        if node is not None:
            print(node.key, end="")
            new_nodes.append(node.left_child)
            new_nodes.append(node.right_child)
        else:
            new_nodes.append(None)
            new_nodes.append(None)
            print(" ", end="")

        print_with_white_spaces(between_spaces)

    print("")

    for i in range(1, end_lines + 1):
        for j in range(len(nodes)):
            print_with_white_spaces(first_spaces - i)
            if nodes[j] is None:
                print_with_white_spaces(end_lines + end_lines + i + 1)
                continue

            if nodes[j].left_child is not None:
                print("/", end="")
            else:
                print_with_white_spaces(1)

            print_with_white_spaces(i + i - 1)

            if nodes[j].right_child is not None:
                print("\\", end="")
            else:
                print_with_white_spaces(1)

            print_with_white_spaces(end_lines + end_lines - i)

        print("")

    print_node_internal(new_nodes, level + 1, max_level)


def print_with_white_spaces(count):
    """
    Print write spaces.
    """
    for i in range(count):
        print(" ", end="")


def get_max_level(node):
    """
    Determine maxlevel (height) of tree.
    """
    if node is None:
        return 0

    return max(get_max_level(node.left_child),
               get_max_level(node.right_child)) + 1


def is_all_elements_null(input_list):
    """
    Check if all elements in input_list are null.
    """
    for obj in input_list:
        if obj is not None:
            return False

    return True
