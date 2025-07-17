# -------------------------------------------------
# File for Tasks A and B
# Class for knapsack
# PLEASE UPDATE THIS FILE
#
# __author__ = 'Edward Small'
# __copyright__ = 'Copyright 2025, RMIT University'
# -------------------------------------------------

import csv
from maze.maze import Maze


class Knapsack:
    """
    Base class for the knapsack.
    """

    def __init__(self, capacity: int, knapsackSolver: str):
        """
        Constructor.

        @param capacity: the maximum weight the knapsack can hold
        @param knapsackSolver: the method we wish to use to find optimal knapsack items (recur or dynamic)
        """
        # initialise variables
        self.capacity = capacity
        self.optimalValue = 0
        self.optimalWeight = 0
        self.optimalCells = []
        self.knapsackSolver = knapsackSolver

    def solveKnapsack(self, maze: Maze, filename: str):
        """
        Calls the method to calculate the optimal knapsack solution
        @param maze: The maze we are considering
        """
        map = []
        # Sort by row (i) first, then column (j)
        sorted_items = sorted(maze.m_items.items(), key=lambda item: (item[0][0], item[0][1]))

        for cell, (weight, value) in sorted_items:
            map.append([cell, weight, value])

        if self.knapsackSolver == "recur":
            self.optimalCells, self.optimalWeight, self.optimalValue = self.recursiveKnapsack(map,
                                                                                              self.capacity,
                                                                                              len(map),
                                                                                              filename)
        elif self.knapsackSolver == "dynamic":
            self.optimalCells, self.optimalWeight, self.optimalValue = self.dynamicKnapsack(map,
                                                                                            self.capacity,
                                                                                            len(map),
                                                                                            filename)

        else:
            raise Exception("Incorrect Knapsack Solver Used.")

    def recursiveKnapsack(self, items: list, capacity: int, num_items: int, filename: str = "results",
                          stats={'count': 0, 'logged': False}):
        """
        Recursive 0/1 Knapsack that logs how many times it's been called
        when the base case is first hit.

        @param items: list of (name, weight, value)
        @param capacity: current remaining knapsack capacity
        @param num_items: number of items still being considered
        @param filename: where to save call count on first base case (used for testing)
        @param stats: dict tracking call count and log status (used for testing)
        """
        # Increment call count on every call - feed back into the function on each call for testing
        stats['count'] += 1

        # delete the below 3 lines if function implemented
        # with open(filename + '.txt', "w") as f:
        #     f.write(str(stats['count']))
        # stats['logged'] = True

        # Base case
        if capacity == 0 or num_items == 0:
            if not stats['logged'] and filename:
                with open(filename+'.txt', "w") as f:
                    f.write(str(stats['count']))
                stats['logged'] = True  # Make sure we only log once
            return [], 0, 0

        """
        IMPLEMENT ME FOR TASK A
        @IMPORTANT
        """

        OptimalLocation = [] # optimal location of treasures to collect
        TotalWeight = 0 # total weight of treasures in knapsack
        OptimalValue = 0 # optimal value given the knapsack capacity 

        # num items = positive integer k of number of treasures
        # capacity = positive integer of maximum weight of knapsack
        # items = list of tuples (location, weight, value) of treasures in the maze

        # OptimalLocation = list of locations of treasures in the knapsack
        # TotalWeight = total weight of treasures in the knapsack
        # OptimalValue = total value of treasures in the knapsack


        # Base: if capacity or num_items (k number of treasures) is 0, return empty list, 0 weight, and 0 value
        if capacity == 0 or num_items == 0:
            return OptimalLocation, TotalWeight, OptimalValue
        
        # calculate location of the last item in the list (index: num_items - 1)
        # calculate the weight and value of the last item in the list (index: num_items - 1)
        location = items[num_items - 1][0]
        weight = items[num_items - 1][1]
        value = items[num_items - 1][2]

        # check if weight is greater than capacityS
        # if it is, we cannot include this item in the knapsack
        # so we call the function again with num_items - 1 (excluding this item)
        if weight > capacity:
            return self.recursiveKnapsack(items, capacity, num_items - 1, filename, stats)

        # Recursive case: check if the last item can be included in the knapsack
        # if it can, check if including it gives a better value than excluding it
        # if it can't, exclude it and check the next item
        include_location, include_weight, include_value = self.recursiveKnapsack(items, capacity - weight, num_items - 1, filename, stats)
        exclude_location, exclude_weight, exclude_value = self.recursiveKnapsack(items, capacity, num_items - 1, filename, stats)

        # check if including the item gives a better value than excluding it
        # if it does, include it in the knapsack and update the total weight and value
        if include_value + value > exclude_value:
            OptimalLocation = include_location + [location]
            TotalWeight = include_weight + weight
            OptimalValue = include_value + value
            
        # if excluding the item gives a better value, exclude it and update the total weight and value
        # if they are equal, we can choose either option
        else:
            OptimalLocation = exclude_location
            TotalWeight = exclude_weight
            OptimalValue = exclude_value

        return OptimalLocation, TotalWeight, OptimalValue


    def dynamicKnapsack(self, items: list, capacity: int, num_items: int, filename: str):
        """
        Dynamic 0/1 Knapsack that saves the dynamic programming table as a csv.

        @param items: list of (name, weight, value)
        @param capacity: current remaining knapsack capacity
        @param num_items: number of items still being considered
        @param filename: save name for csv of table (used for testing)
        """
        # Initialize DP table with None
        dp = [[None] * (capacity + 1) for _ in range(num_items + 1)]
        # first row is all 0s
        dp[0] = [0] * (capacity + 1)

        selected_items, selected_weight, max_value = [], 0, 0

        """
        IMPLEMENT ME FOR TASK B
        @IMPORTANT
        """

        def solveKnapsack(i, w):
            # Base case
            if i == 0 or w == 0:
                dp[i][w] = 0
                return dp[i][w]

            # check if values have already been calculated
            weight, value = items[i - 1][1], items[i - 1][2]

            #  check if weight is greater than capacity 
            if weight > w: 
                dp[i][w] = solveKnapsack(i - 1, w) # if greater, exclude the item
            else:
                # otherwise, include the item and check if it gives a better value by calculating the max value
                dp[i][w] = max(solveKnapsack(i - 1, w), value + solveKnapsack(i - 1, w - weight))
            return dp[i][w]
        
        max_value = solveKnapsack(num_items, capacity)

        # backtrack: find which items were included

        # declarations
        selected_items, selected_weight = [], 0 
        w = capacity

        # backtrack through the dp table to find which items were included
        for i in range(num_items, 0, -1):
            
            if dp[i][w] is not None and dp[i][w] != dp[i - 1][w]: 
                # if the value is not equal to the previous row
                # this means the item was included in the knapsack

                selected_items.append(items[i - 1][0]) # the selected item gets added to the list
                selected_weight += items[i - 1][1] # update the total weight value
                w -= items[i - 1][1] # update the remaining capacity
        
        # Save the DP table to CSV
        print("Saving DP table to CSV...")
        self.saveCSV(dp, items, capacity, filename)

        return selected_items, selected_weight, max_value

    
    def saveCSV(self, dp: list, items: list, capacity: int, filename: str):
        with open(filename+".csv", 'w', newline='') as f:
            writer = csv.writer(f)

            # Header: capacities from 0 to capacity
            header = [''] + [str(j) for j in range(capacity + 1)]
            writer.writerow(header)

            # First row: dp[0], meaning "no items considered"
            first_row = [''] + [(val if val is not None else '#') for val in dp[0]]
            writer.writerow(first_row)

            # Following rows: each item
            for i in range(1, len(dp)):
                row_label = f"({items[i - 1][1]}, {items[i - 1][2]})"
                row = [row_label] + [(val if val is not None else '#') for val in dp[i]]
                writer.writerow(row)

