# Brute-Force
Contains the skeleton code to implement a BFS and DFS. 

You will require the sortedcontainers package. For example, run ```pip install sortedcontainers```

## Learning Objectives

After completing the tasks, you should know the following:

- Learn to implement depth first search (DFS) and breadth first search (BFS) traversal.
- Learn to use breadth first search (BFS) for computing shortest path distances in graphs.

## Tasks
In this lab exercise you will complete the implementation for DFS and BFS traversals starting from a specified seed vertex, and use BFS to compute the shortest path between to vertices in a graph.

### DFS

Depth first search can be implemented as recursive algorithm, as outlined in Algorithm 1. Note that this
is slightly different from what is in the lectures as we are starting the DFS from a seed, while the DFS in
the lecture nodes is seeking to compute the DFS traversal for the whole graph. The implementation in
this workshop will not traverse the whole graph if it is disconnected.

![image](https://github.com/RMIT-COSC2123-3119-AA25/rmit-cosc2123-3119-aa25-classroom-brute-force-Brute-Force/blob/main/img/428429153-1a6ce912-f091-4e5c-869e-614553861e2c.png)

![image](https://github.com/RMIT-COSC2123-3119-AA25/rmit-cosc2123-3119-aa25-classroom-brute-force-Brute-Force/blob/main/img/428429173-969b1ffe-6e10-4602-b052-b2833851448a.png)

### BFS

Breadth first search can be implemented using a queue, which computes the correct order that the vertices
should be visited or processed. Algorithm 2 outlines the approach.

![image](https://github.com/RMIT-COSC2123-3119-AA25/rmit-cosc2123-3119-aa25-classroom-brute-force-Brute-Force/blob/main/img/428429198-fd481254-120d-4011-9748-fe55629473da.png)

### Shortest Path Distance

The shortest path between two vertices in an unweighted graph is the path that traverses the least number
of edges to go from a *source* vertex to a *target* vertex. The shortest path distance between two vertices
is the number of edges traversed in an unweighted graph.

### Computing Shortest Path Distances using BFS

To compute shortest path distances using BFS, a minor modification is needed to the previous pseudo
code for BFS. We know that the neighbours of seed (source) vertex s has distance 0 from s (itself). Its
neighbours have a shortest path distance of 1, their neighbours have a shortest path distance of 2 from
the source vertex and so on.

To implement this, when we enqueue the vertex v, we also need to store the shortest path distance
from s to v, so that when we deque it, then we can just increment the shortest path distance by 1 for its
neighbours.

Shortest path distance using BFS can be implemented as outlined in Algorithm 3.

![image](https://github.com/RMIT-COSC2123-3119-AA25/rmit-cosc2123-3119-aa25-classroom-brute-force-Brute-Force/blob/main/img/428429321-86f16030-c594-4273-a856-1080cd61a0a5.png)

## Information about the code

The programs BFS, DFS and BFSShortestPath reads a sequence of white-space separated integers
from file as edges, construct the corresponding graph. BFS runs breadth first search traversal on the
input graph, DFS runs depth first search traversal and BFSShortestPath computes the shortest path
distance between two input vertices.

![image](https://github.com/RMIT-COSC2123-3119-AA25/rmit-cosc2123-3119-aa25-classroom-brute-force-Brute-Force/blob/main/img/428429488-a35e6de1-1f5b-4377-b692-f4451e7bb5d7.png)

To run BFS, use the command: ```python3 bfs.py <graph fileName> <seed vertex>```

To run DFS, use the command: ```python3 dfs.py <graph fileName> <seed vertex>```

To run BFS Shortest Path, use the command: ```python3 bfs shortest path.py <graph fileName> <source vertex> <target vertex>```

We have provided a sample graph file for you to experiment with. It is called graph1.in. It contains
vertices 0 to 9. Using this file, as an example, you can run BFS on this graph on seed vertex 1 as follows: ```python3 bfs.py graph1.in 1```

# Task

Your task in this lab exercise is to implement the following algorithms in dfs.py, bfs.py and bfs shortest path.py:

1. dfs.py: Implement traverse(Graph g, int s), to compute a depth first traversal from seed vertex “s”.

2. bfs.py: Implement traverse(Graph g, int s), to compute a breadth first traversal from seed vertex “s”.

3. bfs shortest path: Implement spd(Graph g, int s, int t) to compute the shortest path distance between vertices “s” and “t”.
