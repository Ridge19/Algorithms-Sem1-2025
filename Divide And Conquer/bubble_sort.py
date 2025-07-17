from sortutil import swap


def bubble_sort(array):
    """
    Sorts the input array.
    
    @param array Arraylist of integers.   
    """
    # TO BE IMPLEMENTED

    # base case: if array is None or has less than 2 elements, return 0
    if (array is None) or (len(array) < 2):
        return 0
    
    # Debugging output to trace the initial state of the array
    print(f"Initial array: {array}")

    # iterate through the array i
    for i in range (len(array) - 1):
        # iterate through the array j
        for j in range (len(array) - 1 - i):
            # check if we need to swap
            if array[j] > array[j + 1]:
                # swap elements if they are in the wrong order
                swap(array, j, j + 1)
    
    # Print the sorted array
    print(f"Sorted array: {array}")

def main():
    test_list = [5, 4, 3, 9, 1]
    bubble_sort(test_list)
    print(test_list)

    with open('debug.txt') as f:
        array = f.readlines()
    array = [int(item) for item in array]
    bubble_sort(array)
    print(array)


if __name__ == "__main__":
    main()