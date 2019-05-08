s1 = 'abcdefg'
s2 = 'cdeg'

dp = [[0] * (len(s2)+1) for i in range(len(s1)+1)]
# dp[i][j]: s1[i]とs2[j]が共通部分列の何文字目かを格納

maxlen = 0
for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
            maxlen = max(dp[i][j], maxlen)
print (maxlen)
print(dp)
