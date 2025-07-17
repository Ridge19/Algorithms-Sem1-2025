# Empirical Analysis

Contains the skeleton code to experiment with empirical analysis methods

## Learning Objectives

After completing the tasks, you should know the following:

- Able to benchmark algorithms using empirical analysis

## What is empricial analysis?

Evaluation in computer science can be conducted theoretically or empirically. In previous work, we have manipulated equations in order to calculate the estimated number of operations needed to execute an aglorithm. This is analytical (theoretical) analysis.
In this lab, we learn how to apply empirical analysis to a class of similar algorithms by physically timing the run time of functions with different conditions. The efficiency of an algorithm is often measured as the running time. Here we investigate two simple ways to benchmark the performance of a algorithm: the time.time() method call.

## Tasks

### Task A (Knowing what to time)

The aim of task A is to understand how to use timer functions to collect data on the functions you wish to time.

**Bubblesort**

In this part of the lab we will compare the running time of two different BubbleSort implementations
for different input sets. Although we have not covered BubbleSort, the main purpose of the lab is
to explore how to empirically evaluate algorithms, so we can treat them as blackbox algorithms (for
now). The exercise for this part of the lab is to benchmark the run time of the two given implementations ```bubblesort.py``` and ```bubblesort_early_termination.py``` using the given sample data sets
test1.in, test2.in, and test3.in. After the exercise, you will be able to answer the following questions:

1. Which of the two implementations is faster?
2. Is it enough to perform an experiment once? Try running an experiment multiple times and compare the results?
3. How do the two algorithms perform for different input sizes?

First, observe the following code for timing a function called ```count_primes``` (also given to you in this file):
```
def main():
    # set to 40000, can be anything you like
    n = 40000

    start_time = time.time()
    count_primes(n)
    end_time = time.time()

    print(f"Time taken =  {(end_time - start_time):.2f} sec")
```

Notice how we:

1. save the time before calling the function;
2. call the function of interest;
3. save the time after calling the function; and
4. take the difference between these two time points.

In order to empirically analyse bubblesort against early termination, we must do the same thing. Edit ```bubblesort.py``` and ```bubblesort_early_termination.py``` such that they are timed.

You may run the programs with different conditions using the ```file_name.in``` files, e.g.:

```python3 bubblesort.py file_name.in```

### Task B (Comparing Algorithms)

The aim of task B is to know how to use the data from task A to compare to algorithms.

Execution times on a specific machine normally depend upon details of the machine and on the specific
data used. Timings may vary from data set to data set and from machine to machine, so experiments
from one machine and one data set may not be very helpful in general. It is therefore important to
carefully consider the environment in which you benchmark your algorithm. It is common practice to run multiple times
and use the average mean of these results during the evaluation of your experiments.

Run ```bubblesort.py``` and ```bubblesort_early_termination.py``` under various conditions (different problem sizes/problem sets a la test1.in etc). For each problem, do multiple runs and take an average. Plots these results on a graph and comment on
potential complexity between the two variations of buble sort.

### Task C (Knowledge consolidation)

Task C brings these two concepts together on a new algorithm. 

The performance of algorithms is also dependent on the data that it is applied on. Therefore when
evaluating an algorithm, it is also desirable to consider test scenarios that the algorithm could face and
test with representative data samples of these scenarios.

Sometimes it is not possible to obtain real data that covers the important data scenarios. Hence, it is
useful to be able to generate data to test scenarios that we don’t have real data for. In this part of the
lab, we will study two simple ways to generate testing data.

There are many factors to consider, including what values to generate, how many to generate, do we
allow duplicate values and how likely we generate a value. To demonstrate how to generate datasets, we
generate data for the two Bubblesort algorithms. We consider the simple case of generating (non-negative,
or 0 or greater) integers over a range of values that are equally likely to appear in our data samples. This
can be implemented as sampling from a uniform distribution.

We consider two subcases, one where we allow duplicates, one where we do not. In the first subcase
(duplicates are allowed), this is sampling (from a uniform distribution) with replacement. Without
going into details, imagine we have a ball for each integer in the range. We place these balls into a bag,
mix them, then draw/sample one ball. We note down the integer represented by the ball, then drop the
ball back in (leading to the name “with replacement”). We mix them again, and draw again until we
drawn the number of integers (balls) we need.

In the second subcase (only unique values, no duplicates allowed), this is sampling (from a uniform
distribution) without replacement. Using the ball and integer analogy again, this time, when we
draw/sample a ball, we note down the integer of the ball but do not drop the ball back in. We repeat
this process until we have drawn the number of integers (balls) we need. Since the balls are not put back
into the bag, then it the integer it represents can’t be drawn again, so duplicates cannot happen.
Consider the file data generator.py. We have implemented sampling without replacement. Your task
is to implement sampling with replacement to generate data generation that allows duplicates. Complete
the implementation for method sample with ```replacement()```. 

As a hint, consider:

```random.randint(start of the range, end of the range)```

To run the program, type:

```python3 data_generator.py <start of range for values> <end of range for values> <number of values to generate> <with | without>```

where:

- start of range for values: Start of integer range to generate values from (inclusive), must be 0 or greater;
- end of range for values: End of integer range to generate values from (inclusive), must be 0 or greater;
- number of values to generate: Number of values to generate; and
- with — without: using sampling with (without) replacement.


For example

```python3 data_generator.py 1 100 10 with```

will generate a data set of 10 integers ranging from 1 to 100 with replacement active (I can have duplicate integers).
