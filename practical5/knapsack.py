def knapsack_01(weights, values, capacity):
    
    dp = [0] * (capacity + 1)
    
    for i in range(len(weights)):
        
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
            
    return dp[capacity]

if __name__ == "__main__":
    item_values = [60, 100, 120]
    item_weights = [10, 20, 30]
    knapsack_capacity = 50
    
    max_value = knapsack_01(item_weights, item_values, knapsack_capacity)
    print(f"Maximum value obtainable: {max_value}")  
