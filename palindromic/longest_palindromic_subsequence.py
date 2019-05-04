memo = {}
def rec(start, end):
    if start == end:
        return 1
    if (start,end) not in memo:
        if inp[start] == inp[end]:
            memo[(start,end)] = 2 + rec(start+1, end-1)
        else:
            c1 = rec(start+1, end)
            c2 = rec(start, end-1)
            memo[(start,end)] = max(c1, c2)
    return memo[(start, end)]

inp = "abdbca"
start = 0
end = len(inp)-1
print(rec(start, end))
