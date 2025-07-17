import sys

def find(parent, i):
    # Find set of an element i (with path compression)
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    # Union by rank
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskals(graph):
    """
    Kruskal's algorithm to find the Minimum Spanning Tree (MST) of a graph.
    :param graph: A dictionary where keys are node names and values are lists of (neighbor, weight).
    :return: List of edges in the MST and the total weight.
    """
    # Build edge list (avoid duplicates for undirected graph)
    edges = []
    seen = set()
    for node in graph:
        for neighbor, weight in graph[node]:
            if (neighbor, node) not in seen:
                edges.append((weight, node, neighbor))
                seen.add((node, neighbor))

    # Sort edges by weight
    edges.sort()
    parent = {}
    rank = {}
    for node in graph:
        parent[node] = node
        rank[node] = 0

    mst = []
    total_weight = 0
    for weight, u, v in edges:
        if find(parent, u) != find(parent, v):
            mst.append((u, v, weight))
            total_weight += weight
            union(parent, rank, u, v)
    return mst, total_weight

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
    if len(sys.argv) < 2:
        print("Usage: python Kruskals.py <graph_file>")
        sys.exit(1)
    filename = sys.argv[1]
    graph = read_graph_from_file(filename)
    mst, total_weight = kruskals(graph)
    print("Edges in MST:")
    for u, v, weight in mst:
        print(f"{u} - {v}: {weight}")
    print(f"Total weight of MST: {total_weight}")

if __name__ == "__main__":
    main()