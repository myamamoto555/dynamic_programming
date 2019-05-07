def knapsack(c):
    dp = [[0] * (c+1) for i in range(len(weights))] 
    for i in range(len(weights)):
        dp[i][0] = 0
    for i in range(c+1):
        if weights[0] <= i:
            dp[0][i] = profits[0]
    for i in range(1, len(weights)):
        for j in range(1, c+1):
            profit1 = 0
            if j-weights[i] >= 0:
                profit1 = profits[i]+dp[i-1][j-weights[i]]
            profit2 = dp[i-1][j]
            dp[i][j] = max(profit1, profit2)

    return dp[len(weights)-1][c]

weights = [2, 3, 1, 4]
profits = [4, 5, 3, 7]
capacity = 5

print(knapsack(5))
