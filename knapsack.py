def knapsack(values, weights, capacity):
  n = len(values)
  # Create a 2D array dp[][] such that dp[i][j] represents the maximum
  # value that can be obtained by selecting items 1 through i, with a maximum
  # weight of j.
  dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

  for i in range(1, n + 1):
    for j in range(1, capacity + 1):
      if weights[i - 1] > j:
        # If the weight of the current item is greater than the maximum weight,
        # we cannot select it.
        dp[i][j] = dp[i - 1][j]
      else:
        # Otherwise, we have two options: we can either select the current item
        # or not. We choose the option that results in the maximum value.
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])

  return dp[n][capacity]
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
print(knapsack(values, weights, capacity))  
