# This code implements Dijkstra's algorithm to find the shortest paths from a starting node to all other nodes in a graph.
# The graph is represented as a dictionary where keys are node names and values are lists of tuples containing neighboring nodes and their respective edge weights.
# The algorithm uses a priority queue to efficiently retrieve the next node with the smallest distance.
# The distances are updated only if a shorter path is found, ensuring that the algorithm runs efficiently.
# The example usage demonstrates how to call the Dijkstra's function with a sample graph and starting node.
# The output will show the shortest distances from the starting node to all other nodes in the graph.
# The code is structured to be easily testable and can be integrated into larger applications or used for educational purposes.

import sys

def Dijkstras(graph, start):
    """
    Implements Dijkstra's algorithm to find the shortest path from the start node to all other nodes in the graph.
    
    :param graph: A dictionary representing the graph where keys are node names and values are lists of tuples (neighbor, weight).
    :param start: The starting node for the algorithm.
    :return: A dictionary with the shortest distance from the start node to each node.
    """
    import heapq

    # Priority queue to store (distance, node)
    queue = []
    heapq.heappush(queue, (0, start))
    
    # Dictionary to store the shortest distance to each node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        # Nodes can only be processed once
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    return distances

def read_graph_from_file(filename):
    """
    Reads a graph from a text file.
    Each line: Node Neighbor1,Weight1 Neighbor2,Weight2 ...
    Returns a dictionary graph.
    """
    graph = {}
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if not parts:
                continue
            node = parts[0]
            neighbors = []
            for neighbor_info in parts[1:]:
                neighbor, weight = neighbor_info.split(',')
                neighbors.append((neighbor, int(weight)))
            graph[node] = neighbors
    return graph

def main():
    if len(sys.argv) < 3:
        print("Usage: python Dijkstras.py <graph_file> <start_node>")
        sys.exit(1)
    filename = sys.argv[1]
    start_node = sys.argv[2]
    graph = read_graph_from_file(filename)
    shortest_paths = Dijkstras(graph, start_node)
    print(f"Shortest paths from {start_node}: {shortest_paths}")

if __name__ == "__main__":
    main()




