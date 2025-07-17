import sys
import time

def bubble_sort_optimized(numbers):
    """
    Early Termination bubble sort.
    
    @param numbers list of integers.   
    """
    swapped = False
    remain_len = len(numbers)
    swapped = True

    while swapped:
        swapped = False
        for i in range(remain_len - 1):
            # check if we need to swap
            if numbers[i] > numbers[i+1]:
                temp = numbers[i]
                numbers[i] = numbers[i+1]
                numbers[i+1] = temp
                swapped = True

        remain_len -= 1



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 bubblesort_optimized.py file_name")
        exit()

    file_name = sys.argv[1]
    with open(file_name) as f:
        numbers_str = f.readlines()

    numbers = [int(number) for number in numbers_str]
    print(f"Original numbers: {numbers}")
    bubble_sort_optimized(numbers)
    print(f"After bubble sort (early termination): {numbers} \n")
    print("Size of array = " + str(len(numbers)))    


if __name__ == "__main__":
    main()
