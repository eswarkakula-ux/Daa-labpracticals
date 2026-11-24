INF = float("inf")


def tsp(dist):
    n = len(dist)
    memo = {}

    def visit(city, visited):
        if visited == (1 << n) - 1:
            return dist[city][0] if dist[city][0] > 0 else INF

        state = (city, visited)
        if state in memo:
            return memo[state]

        min_cost = INF
        for next_city in range(n):
            if not (visited & (1 << next_city)) and dist[city][next_city] > 0:
                cost = dist[city][next_city] + visit(
                    next_city, visited | (1 << next_city)
                )
                if cost < min_cost:
                    min_cost = cost

        memo[state] = min_cost
        return min_cost

    return visit(0, 1)


if __name__ == "__main__":
    graph = [,
 ,
 ,
 ,
 ,
    ]

    min_tour_cost = tsp(graph)
    print(f"Minimum tour cost: {min_tour_cost}")
