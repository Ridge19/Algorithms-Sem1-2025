from sortutil import *
import math
import sys

"""
 * Implementation of Quicksort, same as the lecture notes.
 * Use first element as pivot.
 * 
"""


def quick_sort(array):
    """
    * Sort array.
    * 
    * @param array Array to be sorted.   
    """

    # TO BE IMPLEMENTED

    # base case: if array is None or has less than 2 elements, return 0
    if (array is None) or (len(array) < 2):
        return 0
    
    # choose pivot as first element
    pivot = array[0]

    # Debugging output to trace the pivot selection
    print(f"Choosing pivot: {pivot} from {array}")

    # compare each element with pivot
    less_than_pivot = []
    greater_than_pivot = []
    for item in array[1:]:
        if item < pivot:
            less_than_pivot.append(item)
        else:
            greater_than_pivot.append(item)
    
    # Debugging output to trace the partitioning process
    print(f"Partitioning: {array} into {less_than_pivot} and {greater_than_pivot} with pivot {pivot}")

    # recursively sort less_than_pivot and greater_than_pivot
    quick_sort(less_than_pivot)
    quick_sort(greater_than_pivot)

    # combine sorted parts with pivot
    array[:] = less_than_pivot + [pivot] + greater_than_pivot

    # Debugging output to trace the final sorted array
    print(f"Sorted array: {array}")




def main():
    test_list = [5, 4, 3, 9, 1]
    quick_sort(test_list)
    print(test_list)

    with open('debug.txt') as f:
        array = f.readlines()
    array = [int(item) for item in array]
    quick_sort(array)
    print(array)


if __name__ == "__main__":
    main()
