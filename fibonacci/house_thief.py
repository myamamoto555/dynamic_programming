house = [2, 10, 14, 8, 1]

dp = [0] * len(house)

dp[0] = house[0]
dp[1] = max(house[0], house[1])

for i in range(2, len(house)):
    dp[i] = max(dp[i-2]+house[i], dp[i-1])

print(dp[len(house)-1])
