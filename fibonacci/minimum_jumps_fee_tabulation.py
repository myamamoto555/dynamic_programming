fee = [2,3,4,5]

dp = [float('inf')] * len(fee)

dp[0] = 0
dp[1] = fee[0]
dp[2] = fee[0]
dp[3] = fee[0]

for i in range(4, len(fee)):
    dp[i] = min(dp[i-3]+fee[i-3], dp[i-2]+fee[i-2], dp[i-1]+fee[i-1])

print(dp)
print(dp[len(fee)-1])
