"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

This program demonstrates Breadth-First Search using a simple
graph that represents locations connected by roads.
===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    Performs Breadth-First Search on a graph and returns
    the order in which the nodes are visited.
    """

    # If the starting node does not exist, return an empty list.
    if start not in graph:
        return []

    # A set keeps track of nodes that have already been visited.
    visited = set()

    # A queue is used because BFS visits nodes in the order
    # they are discovered. The first node added is the first removed.
    queue = deque([start])

    # Stores the final traversal order.
    traversal_order = []

    while queue:
        current = queue.popleft()

        if current not in visited:
            visited.add(current)
            traversal_order.append(current)

            # Neighbors are added to the queue so BFS can visit
            # all nearby nodes before moving farther away.
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)

    # BFS explores level by level, while depth-first search (DFS)
    # follows one path as deeply as possible before backtracking.
    return traversal_order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # This graph represents cities connected by roads.
    # Each city is a node, and each road is an edge.
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"]
    }

    print("\n=== GRAPH STRUCTURE ===")

    # Display each node and its connected neighbors.
    for node, neighbors in graph.items():
        print(node, "->", neighbors)

    # ===============================
    # BFS TRAVERSAL
    # ===============================

    print("\n=== BFS TRAVERSAL ===")

    start_node = "A"

    # Starting at A, BFS first visits A, then its immediate
    # neighbors, and then nodes that are farther away.
    result = bfs(graph, start_node)

    print("Starting node:", start_node)
    print("BFS traversal:", result)

    # Add a new node and edge to the graph.
    # G is connected to C.
    graph["G"] = ["C"]
    graph["C"].append("G")

    print("\nAfter adding node G connected to C:")
    updated_result = bfs(graph, start_node)
    print("Updated BFS traversal:", updated_result)

    # ===============================
    # EDGE CASE TESTS
    # ===============================

    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1:
    # Start BFS from a different node.
    # The traversal still works, but the visiting order changes.
    print("\nEdge Case 1: Start from node E")
    print("Traversal:", bfs(graph, "E"))

    # Edge Case 2:
    # Attempt to start from a node that does not exist.
    # The bfs function safely returns an empty list.
    print("\nEdge Case 2: Missing starting node")
    print("Traversal:", bfs(graph, "Z"))


if __name__ == "__main__":
    main()