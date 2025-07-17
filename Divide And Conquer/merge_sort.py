import math


def merge_sort(array):
    """
    sort array

    @param array Array to be sorted
    """

    # TO BE IMPLEMENTED

    # base case: if array is None or has less than 2 elements, return 0
    if (array is None) or (len(array) < 2):
        return 0
    
    # split array into halves recursively
    left_half = array[:len(array) // 2] 
    right_half = array[len(array) // 2:]

    # Debugging output to trace the splitting and merging process
    print(f"Splitting: {array} into {left_half} and {right_half}")

    # Recursively sort both halves
    merge_sort(left_half)
    merge_sort(right_half)

    # declarations
    i = j = k = 0

    # when left_half and right_half are less than i and j respectively
    while i < len(left_half) and j < len(right_half):
        # if left_half[i] is less than or equal to right_half[j], assign left_half[i] to array[k] and increment i
        # else assign right_half[j] to array[k] and increment j
        if left_half[i] <= right_half[j]:
            array[k] = left_half[i]
            i += 1
        else:
            array[k] = right_half[j]
            j += 1
        k += 1
    
    # if left_half is still < i
    while i < len(left_half):
        # assign left_half[i] to array[k] and increment i and k
        array[k] = left_half[i]
        i += 1
        k += 1
    # if right_half is still < j
    # assign right_half[j] to array[k] and increment j and k
    while j < len(right_half):
        array[k] = right_half[j]
        j += 1
        k += 1
    
    # Debugging output to trace the merging process
    print(f"Merging: {left_half} and {right_half} into {array}")


# Main function to test the merge_sort implementation
def main():
    test_list = [5, 4, 3, 9, 1]
    merge_sort(test_list)
    print(test_list)

    with open('debug.txt') as f:
        array = f.readlines()
    array = [int(item) for item in array]
    merge_sort(array)
    print(array)


if __name__ == "__main__":
    main()
