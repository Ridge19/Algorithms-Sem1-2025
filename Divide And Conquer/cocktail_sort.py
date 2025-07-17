from sortutil import *


def cocktail_sort(array):
    """
    * Sort array.
    *
    * @param array Array to be sorted.
    """

    begin = 0
    end = len(array) - 1
    swapped = True

    while swapped:
        swapped = False
        # left to right 
        for i in range(begin, end):
            if array[i] > array[i + 1]:
                swap(array, i + 1, i)
                swapped = True

        # if no swap occurred, we are done
        if not swapped:
            break

        swapped = False
        end -= 1

        # right to left 
        for i in range(end, begin, -1):
            if array[i] < array[i - 1]:
                swap(array, i - 1, i)
                swapped = True
        begin += 1


def main():
    test_list = [5, 4, 3, 9, 1]
    cocktail_sort(test_list)
    print(test_list)

    with open('debug.txt') as f:
        array = f.readlines()
    array = [int(item) for item in array]
    cocktail_sort(array)
    print(array)


if __name__ == "__main__":
    main()
