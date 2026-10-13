import sys

def matrix_chain_order(dims):
    """
    dims: list of matrix dimensions where matrix i has dimensions dims[i-1] x dims[i]
    For n matrices, dims should have n+1 elements.
    e.g. dims = [40, 20, 30, 10, 30] means:
        A1: 40x20, A2: 20x30, A3: 30x10, A4: 10x30
    Returns: (min_cost, split_table)
    """
    n = len(dims) - 1  # number of matrices
    
    # dp[i][j] = min number of scalar multiplications to compute A_i...A_j
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    split = [[0] * (n + 1) for _ in range(n + 1)]
    
    # chain_len is the length of the chain being considered
    for chain_len in range(2, n + 1):
        for i in range(1, n - chain_len + 2):
            j = i + chain_len - 1
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                cost = (dp[i][k] + dp[k + 1][j] +
                        dims[i - 1] * dims[k] * dims[j])
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k
    
    return dp[1][n], split


def print_optimal_parens(split, i, j):
    """Reconstructs the optimal parenthesization as a string."""
    if i == j:
        return f"A{i}"
    else:
        k = split[i][j]
        left = print_optimal_parens(split, i, k)
        right = print_optimal_parens(split, k + 1, j)
        return f"({left} x {right})"


if __name__ == "__main__":
    # Example: 4 matrices A1(40x20), A2(20x30), A3(30x10), A4(10x30)
    dims = [40, 20, 30, 10, 30]
    n = len(dims) - 1
    
    min_cost, split = matrix_chain_order(dims)
    
    print(f"Minimum number of multiplications: {min_cost}")
    print(f"Optimal parenthesization: {print_optimal_parens(split, 1, n)}")
