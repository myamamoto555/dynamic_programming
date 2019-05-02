memo = {}
def rec(item, c):
    if c > capacity or item >= len(profits):
        return 0
    if (item, c) in memo:
        return memo[(item, c)]
    profit1 = 0
    if c-weights[item] >= 0:
        profit1 = profits[item] + rec(item, c - weights[item])
    profit2 = rec(item + 1, c)
    memo[(item, c)] = max(profit1, profit2)
    return memo[(item, c)]

weights = [1,2,3]
profits = [15, 20, 50]
capacity = 5

print (rec(0, capacity))
