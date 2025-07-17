import heapq

def Prims(graph, start):
    """
    Prim's algorithm to find the Minimum Spanning Tree (MST) of a graph.
    :param graph: A dictionary where keys are node names and values are lists of (neighbor, weight).
    :param start: The starting node for the algorithm.
    :return: List of edges in the MST and the total weight.
    """
    mst = []
    total_weight = 0
    visited = set()
    min_heap = [(0, start, None)]  # (weight, current_node, parent_node)

    while min_heap:
        weight, current, parent = heapq.heappop(min_heap)
        if current not in visited:
            visited.add(current)
            if parent is not None:
                mst.append((parent, current, weight))
                total_weight += weight

            for neighbor, edge_weight in graph.get(current, []):
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_weight, neighbor, current))

    return mst, total_weight

def read_graph_from_file(filename):
    """
    Reads a graph from a text file.
    Each line: Node Neighbor1,Weight1 Neighbor2,Weight2 ...
    Returns a dictionary graph.
    """
    graph = {}
    with open(filename) as f:
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
    if len(sys.argv) < 2:
        print("Usage: python Prims.py <graph_file>")
        sys.exit(1)
    filename = sys.argv[1]
    graph = read_graph_from_file(filename)
    start_node = next(iter(graph))  # Get an arbitrary start node
    mst, total_weight = Prims(graph, start_node)
    print("Edges in MST:")
    for u, v, weight in mst:
        print(f"{u} - {v}: {weight}")
    print(f"Total weight of MST: {total_weight}")
    
if __name__ == "__main__":
    import sys
    main()