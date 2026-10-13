def min_coins_for_change(coins, target):

    dp = [float('inf')] * (target + 1)
  
    dp[0] = 0
 
    for amount in range(1, target + 1):
        for coin in coins:
            if amount - coin >= 0:

                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
                
    return dp[target] if dp[target] != float('inf') else -1

coin_denominations = [1, 2, 5]
target_amount = 11
print(f"Minimum coins needed: {min_coins_for_change(coin_denominations, target_amount)}")
