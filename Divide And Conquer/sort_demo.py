from bubble_sort import *
from cocktail_sort import *
from merge_sort import *
from quick_sort import *
import time
import sys

"""
 * Demonstrate the different sorting algorithms.
"""


def print_usage(prog_name):
    print(f"USAGE: {prog_name} [sort method] [input file]")
    print(f"  sort methods [bubble, quick, merge, cocktail]")
    print(f"EXAMPLE: {prog_name} quick random.txt")


def main():
    """
    * Main method.
    """

    prog_name = "SortDemo"
    args = sys.argv[1:]

    # not enough arguments
    if args.__len__() != 2:
        print_usage(prog_name)
        exit(1)

    # sorting algorithm to be used
    algorithm_used = args[0]
    # input file to be sorted
    file_name = args[1]

    with open(file_name) as in_file:
        values = in_file.readlines()

    # create array of int
    array = [int(item) for item in values]

    # figure out with sorting algorithm we are using
    if algorithm_used == "bubble":
        sort_alg = bubble_sort
        # sort_"bub"ble(dataset->data,dataset->items)
    elif algorithm_used == "cocktail":
        sort_alg = cocktail_sort
    elif algorithm_used == "merge":
        sort_alg = merge_sort
    elif algorithm_used == 'quick':
        sort_alg = quick_sort
    else:
        print(f"Error: {algorithm_used} is invalid.")
        array = None
        print_usage(prog_name)
        exit(1)

    start_time = time.time_ns()

    # do the sorting
    sort_alg(array)

    end_time = time.time_ns()

    # print out sorted array
    print(array)

    time_elapsed = (end_time - start_time) / math.pow(10, 9)
    print(f"Time elapsed (secs): {time_elapsed}")


if __name__ == "__main__":
    main()
