inp = 'cddpd'

dp = [[0] * len(inp) for i in range(len(inp))]
for i in range(len(inp)):
    dp[i][i] = 1

for i in range(len(inp)-2, -1, -1):
    for j in range(i+1, len(inp)):
        if inp[i] == inp[j]:
            dp[i][j] = 2 + dp[i+1][j-1]
        else:
            dp[i][j] = max(dp[i+1][j], dp[i][j-1])
print(dp[0][len(inp)-1])
print(dp)
