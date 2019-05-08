inp = 'cddpddc'

dp = [[False] * len(inp) for i in range(len(inp))]

for i in range(len(inp)):
    dp[i][i] = True

maxlen = 0
for i in range(len(inp)-1, -1, -1):
    for j in range(i+1, len(inp)):
        if inp[i] == inp[j] and dp[i+1][j-1]:
            dp[i][j] = True
            maxlen = max(maxlen, j-i+1)
print(maxlen)
