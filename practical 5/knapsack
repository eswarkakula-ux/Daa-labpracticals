def knapsack_01(weights, values, capacity):
    dp = [0] * (capacity + 1)
    
    for i in range(len(weights)):
        
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
            
    return dp[capacity]

if __name__ == "__main__":
    print("--- 0/1 Knapsack Calculator ---")
    
    item_values = list(map(int, input("Enter item values separated by spaces: ").split()))
    
    item_weights = list(map(int, input("Enter item weights separated by spaces: ").split()))
    
    knapsack_capacity = int(input("Enter the maximum knapsack capacity: "))
    
    if len(item_values) != len(item_weights):
        print("\nError: The number of values must match the number of weights!")
    else:
        max_value = knapsack_01(item_weights, item_values, knapsack_capacity)
        print(f"\nMaximum value obtainable: {max_value}")
 
