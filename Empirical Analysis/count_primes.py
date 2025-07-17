import time
import math

def count_primes(n):
    """
    Count the number of primes smaller than n
    """
    count = 0

    # loop from 2 to n-1, and try each subsequent i as a prime
    for i in range(2, n):
        np = False
        for j in range(2, i):
            # test if prime
            if i % j == 0 :
                np = True
                break

            # increment prime count
            if not np:
                count+=1
            
        
     # end of outer for loop

    return count

def main():
    # set to 40000, can be anything you like
    n = 40000

    start_time = time.time()
    count_primes(n)
    end_time = time.time()

    print(f"Time taken =  {(end_time - start_time):.2f} sec")

if __name__ == "__main__":
    main()