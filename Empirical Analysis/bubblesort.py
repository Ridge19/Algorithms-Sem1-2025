import sys
import time

# ------------------------------------------
# Standard bubble sort, no early termination
# ------------------------------------------

def bubble_sort(numbers):
    """
    Sorts the input numbers.
    
    @param numbers list of integers.   
    """
    for i in range(len(numbers)): 
        for j in range(len(numbers)-1): 
            # check if we need to swap
            if (numbers[j] > numbers[j+1]):
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 bubblesort.py file_name")
        exit()
    file_name = sys.argv[1]
    with open(file_name) as f:
        numbers_str = f.readlines()
    numbers = [int(number) for number in numbers_str]
    print(f"Original numbers: {numbers}")
    bubble_sort(numbers)
    print(f"After bubble sort: {numbers} \n")
    print("Size of array = " + str(len(numbers)))    

if __name__ == "__main__":
    main()
