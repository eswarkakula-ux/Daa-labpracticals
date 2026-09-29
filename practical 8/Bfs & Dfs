import time
from collections import deque


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def _dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=" ")

        for neighbor in self.adj[v]:
            if not visited[neighbor]:
                self._dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = [False] * self.V
        self._dfs_util(start, visited)

    def bfs(self, start):
        visited = [False] * self.V
        queue = deque()

        visited[start] = True
        queue.append(start)

        while queue:
            node = queue.popleft()
            print(node, end=" ")

            for neighbor in self.adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)


def main():
    V = int(input("Enter number of vertices: "))

    if V <= 0:
        print("Number of vertices must be greater than 0.")
        return

    graph = Graph(V)

    E = int(input("Enter number of edges: "))

    if E < 0:
        print("Number of edges cannot be negative.")
        return

    print("Enter edges (u v):")

    for _ in range(E):
        u, v = map(int, input().split())

        if 0 <= u < V and 0 <= v < V:
            graph.add_edge(u, v)
        else:
            print(f"Invalid edge: {u} {v}")
            return

    start = int(input("Enter starting vertex: "))

    if not (0 <= start < V):
        print("Invalid starting vertex.")
        return

    # DFS
    start_dfs = time.perf_counter_ns()

    print("\nDFS Traversal: ", end="")
    graph.dfs(start)

    end_dfs = time.perf_counter_ns()
    dfs_time = end_dfs - start_dfs

    # BFS
    start_bfs = time.perf_counter_ns()

    print("\nBFS Traversal: ", end="")
    graph.bfs(start)

    end_bfs = time.perf_counter_ns()
    bfs_time = end_bfs - start_bfs

    # Execution time
    print("\n\nExecution Time:")
    print(f"DFS: {dfs_time} ns")
    print(f"BFS: {bfs_time} ns")


if __name__ == "__main__":
    main()
