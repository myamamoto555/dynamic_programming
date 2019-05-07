ele = [1,1,3,6,9,3,0,1,3]

dp = [float('inf')] * len(ele)
dp[0] = 0

for start in range(len(ele)-1):
    for end in range(1, len(ele)):
        if end <= start + ele[start]:
            dp[end] = min(dp[start]+1, dp[end])

print (dp[len(ele)-1])
