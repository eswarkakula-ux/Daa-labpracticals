import heapq
def prims_algorithm(graph):
    n=len(graph)
    visited = [False] * n
    pq=[(0,0)]
    total_cost=0
    while pq:
        cost, node = heapq.heappop(pq)
        if visited[node]:
            continue
        visited[node] = True
        total_cost += cost
        for neighbor, weight in graph[node]:
            if not visited[neighbor]:
                heapq.heappush(pq, (weight, neighbor))
    return total_cost
if __name__ == "__main__":
    graph = {
        0: [(1, 2), (3, 6)],
        1: [(0, 2), (2, 3), (3, 8), (4, 5)],
        2: [(1, 3), (4, 7)],
        3: [(0, 6), (1, 8), (4, 9)],
        4: [(1, 5), (2, 7), (3, 9)]
    }
    print(prims_algorithm(graph))
