# -------------------------------------------------------------------
# PLEASE UPDATE THIS FILE.
# Greedy maze solver for all entrance, exit pairs
#
# __author__ = <student name here>
# __copyright__ = 'Copyright 2025, RMIT University'
# -------------------------------------------------------------------


from maze.util import Coordinates
from maze.maze import Maze

from knapsack.knapsack import Knapsack
from itertools import permutations

from typing import List, Dict, Optional

from collections import deque
from maze.util import Coordinates


class TaskDSolver:
    def __init__(self, knapsack:Knapsack):
        self.m_solverPath: List[Coordinates] = []
        self.m_cellsExplored = 0 # count of UNIQUE cells visited. i.e. final count should equal len(set(self.m_solverPath))
        self.m_entranceUsed = None
        self.m_exitUsed = None
        self.m_knapsack = knapsack
        self.m_value = 0
        self.m_reward = float('-inf') # initial reward should be terrible

        # you may which to add more parameters here, such as probabilities, etc
        # you may update these parameters using the Maze object in SolveMaze

    def reward(self):
        return self.m_knapsack.optimalValue - self.m_cellsExplored

    def solveMaze(self, maze: Maze, entrance: Coordinates, exit: Coordinates):
        """
        Solution for Task D goes here.

        Be sure to increase self.m_cellsExplored whenever you visit a NEW cell
        Be sure to increase the knapsack_value whenever you find an item and put it in your knapsack.
        You may use the maze object to check if a cell you visit has an item
        maze.m_itemParams can be used to calculate things like predicted reward, etc. But you can only use
        maze.m_items to check if your current cell contains an item (and if so, what is its weight and value)

        Code in this function will be rigorously tested. An honest but bad solution will still gain quite a few marks.
        A cheated solution will gain 0 marks for all of Task D.
        Args:
            maze: maze object
            entrance: initial entrance coord
            exit: exit coord

        Returns: Nothing, but updates variables
        -------------------------
        Solution: 
        Use BFS to find the shortest path from entrance to exit. avoiding walls and collecting items (treasures) along the way
        use BFS to find the nearest unexplored cell and explore it (check for treasure)
        use a greedy programming approach and collect items (treasures) along the way, regardless of the value. 
            - unless knapsack is full (weight exceeds capacity)
            - or all items are collected
        use a knapsack to keep track of the items collected and their total weight and value. 
            - when collecting an item, check if the total weight exceeds the knapsack capacity. if it does, leave it. otherwise add it to the knapsack

        """

        # initialize knapsack values
        self.m_knapsack.optimalCells = [] # list of cells where items were collected
        self.m_knapsack.optimalValue = 0 # total value of items in the knapsack (opitmal values)
        self.m_knapsack.optimalWeight = 0 # total weight of items in the knapsack (optimal weight)

        # BFS to find the shortest path from entrance to exit
        def bfs_to_nearest_unexplored(start, explored):
            """ Find the nearest unexplored cell from the start position."""
            queue = deque() # using deque for efficient FIFO queue
            queue.append((start, [start])) # start with entrance
            visited = set() # create set to keep track of visited cells
            visited.add(start) # mark entrance as visited

            # BFS loop
            while queue:
                current, path = queue.popleft() # dequeue the first element
                # Only use getRow/getCol for keys
                i, j = current.getRow(), current.getCol() # get coordinates of current cell
                item = maze.m_items.get((i, j)) # get item at current cell (if item is present)
                if current not in explored: # if current cell is unexplored
                    return path # return path to the unexplored cell
                for neighbor in maze.neighbours(current): # get neighbors of current cell
                    if isinstance(neighbor, tuple): # convert tuple to Coordinates
                        neighbor = Coordinates(*neighbor) # convert tuple to Coordinates to get neighbor coordinates
                    if neighbor not in visited and not maze.hasWall(current, neighbor): # if neighbor is not visited and has no wall
                        visited.add(neighbor) # add neighbor to visited set 
                        queue.append((neighbor, path + [neighbor])) # enqueue the neighbor with the path to it
            # if no unexplored cell is found, return empty list
            return []
        
        def bfs_path(start, goal, explored):
            """Find shortest path from entrance to exit, avoiding walls."""
            queue = deque() # using deque for efficient FIFO queue
            queue.append((start, [start])) # start with entrance
            visited = set() # to keep track of visited cells
            visited.add(start) # mark entrance as visited
            while queue:
                current, path = queue.popleft() # dequeue the first element
                i, j = current.getRow(), current.getCol()
                item = maze.m_items.get((i, j))
                if current == goal: # if exit is reached, return path
                    return path
                for neighbor in maze.neighbours(current): # otherwise, get neighbors of current cell
                    if isinstance(neighbor, tuple): 
                        neighbor = Coordinates(*neighbor) # convert tuple to Coordinates to get neighbor coordinates
                    if neighbor not in visited and not maze.hasWall(current, neighbor): # if neighbor is not visited and has no wall
                        visited.add(neighbor) # add neighbor to visited set
                        queue.append((neighbor, path + [neighbor])) # enqueue the neighbor with the path to it
            return [] # return empty list if no path found

        # initialize variables
        current = entrance # set entrance as current position
        explored = set([entrance]) # add entrance to explored set
        path = [entrance] # initialize path with entrance
        knapsack_weight = self.m_knapsack.optimalWeight # total weight of items in the knapsack
        knapsack_value = self.m_knapsack.optimalValue # total value of items in the knapsack
        collected = set() # set to keep track of collected items

        # while loop to explore the maze
        # continue until current position is exit, all knapsack items are collected or all cells are explored
        while current != exit:
            # Only discover a treasure when stepping on a cell
            i, j = current.getRow(), current.getCol()
            if hasattr(maze, 'm_items') and (i, j) in maze.m_items and current not in collected: # check if current cell has an item
                item_weight, item_value = maze.m_items[(i, j)] # get item at current cell (if item is present)
                if knapsack_weight + item_weight <= self.m_knapsack.capacity: # check if adding item to knapsack exceeds capacity
                    knapsack_weight += item_weight # if not, add item to knapsack
                    knapsack_value += item_value # update knapsack value
                    collected.add(current) # add current cell to collected set
                    self.m_knapsack.optimalValue = knapsack_value  # update knapsack value as you collect
                    self.m_knapsack.optimalWeight = knapsack_weight # update knapsack weight as you collect
                    self.m_knapsack.optimalCells.append((i, j)) # add current cell to knapsack optimal cells
                    self.m_reward = self.reward() # update reward

            # check if agent should exit 
            should_exit = (
                len(collected) == getattr(maze, 'm_numItems', len(collected)) or # all items collected
                knapsack_weight >= self.m_knapsack.capacity or # knapsack is full (weight exceeds capacity)
                len(explored) >= maze.m_rows * maze.m_cols # all cells explored / no treasure left
            )
            # use argument unpacking to convert a tuple into Coordinates object. (*n)
            # in python, a tuple is a ordered collection of elements, similar to a list.
            if exit in [Coordinates(*n) if isinstance(n, tuple) else n for n in maze.neighbours(current)] \
                    and not maze.hasWall(current, exit) and should_exit: # check if exit is reachable
                path.append(exit) # add exit to path
                explored.add(exit) # add exit to explored set 
                current = exit # set exit as current position
                break # exit loop

            # if exit is not reachable, find the nearest unexplored cell
            next_segment = bfs_to_nearest_unexplored(current, explored)
            if not next_segment:
                to_exit = bfs_path(current, exit, explored) # find path to exit
                if not to_exit:
                    break # no path to exit found, break loop
                if to_exit: #if exit path is found
                    for cell in to_exit[1:]: # skip the first cell (current position)
                        path.append(cell) # add cell to path
                        explored.add(cell) # add cell to explored set
                        current = cell # set cell as current position
                        i, j = current.getRow(), current.getCol() # get coordinates of current cell
                        if hasattr(maze, 'm_items') and (i, j) in maze.m_items and current not in collected: # check if current cell has an item
                            item_weight, item_value = maze.m_items[(i, j)] # get item at current cell (if item is present)
                            if knapsack_weight + item_weight <= self.m_knapsack.capacity: # same as function above. please see comments. 
                                knapsack_weight += item_weight
                                knapsack_value += item_value
                                collected.add(current)
                                self.m_knapsack.optimalValue = knapsack_value
                                self.m_knapsack.optimalWeight = knapsack_weight
                                self.m_knapsack.optimalCells.append((i, j))
                                self.m_reward = self.reward()
                    break # exit is reachable, break loop

            # same as above. please see comments.
            for cell in next_segment[1:]:
                path.append(cell)
                explored.add(cell)
                current = cell
                i, j = current.getRow(), current.getCol()
                if hasattr(maze, 'm_items') and (i, j) in maze.m_items and current not in collected:
                    item_weight, item_value = maze.m_items[(i, j)]
                    if knapsack_weight + item_weight <= self.m_knapsack.capacity:
                        knapsack_weight += item_weight
                        knapsack_value += item_value
                        collected.add(current)
                        self.m_knapsack.optimalValue = knapsack_value
                        self.m_knapsack.optimalWeight = knapsack_weight
                        self.m_knapsack.optimalCells.append((i, j))
                        self.m_reward = self.reward()
                
                if current == exit: # if exit is reached, break loop
                    break

        # update the solver path, entrance, exit, cells explored, and reward after.
        self.m_solverPath = path
        self.m_entranceUsed = entrance
        self.m_exitUsed = exit
        self.m_cellsExplored = len(set(path))
        self.m_reward = self.reward()
        self.m_collected = collected

        # TESTING - CHECK PATH LEGALITY ACCORDING TO REQUIREMENTS
        self.checkPathLegal(maze, entrance, exit)

    def checkPathLegal(self, maze:Maze, entrance:Coordinates, exit:Coordinates):
        """
        Checks if the generated path is legal. Throws an error if not.
        Also checks that the path starts at the entrance and ends at the exit.
        """
        if not self.m_solverPath:
            raise ValueError("Illegal path: Path is empty.")

        # Check start and end positions
        if self.m_solverPath[0] != entrance:
            raise ValueError(
                f"Illegal path: Path does not start at entrance ({entrance.getRow()}, {entrance.getCol()})."
            )
        if self.m_solverPath[-1] != exit:
            raise ValueError(
                f"Illegal path: Path does not end at exit ({exit.getRow()}, {exit.getCol()})."
            )

        # LEGAL PATH CHECK
        for i in range(1, len(self.m_solverPath)):
            prev = self.m_solverPath[i - 1]
            curr = self.m_solverPath[i]
            # Check adjacency
            if curr not in maze.neighbours(prev):
                raise ValueError(
                    f"Illegal path: ({prev.getRow()}, {prev.getCol()}) and ({curr.getRow()}, {curr.getCol()}) are not adjacent."
                )
            # Check for wall
            if maze.hasWall(prev, curr):
                raise ValueError(
                    f"Illegal path: Wall between ({prev.getRow()}, {prev.getCol()}) and ({curr.getRow()}, {curr.getCol()})."
                )

        print("Path is legal.")