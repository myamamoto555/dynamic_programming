nums = [-4, 10, 3, -5, 7, 15]

dp = [1] * len(nums)  # dp[i]: nums[i]を含めた場合の最長増加列


maxlen = 0
for i in range(len(nums)):
    for j in range(i):
        if nums[i] > nums[j] and dp[i] <= dp[j]:
            dp[i] = dp[j] + 1
            maxlen = max(maxlen, dp[i])
print(dp)
