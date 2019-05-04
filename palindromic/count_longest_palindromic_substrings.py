def palindrome_check(s,e):
    while(s<=e):
        if inp[s] != inp[e]:
            return False
        s += 1
        e -= 1
    return True

memo = {}
def rec(s, e):
    if s > e:
        return 0
    if s == e:
        return 1
    if (s,e) not in memo:
        if palindrome_check(s,e):
            memo[(s,e)] = rec(s+1,e) + rec(s,e-1) + 1 - rec(s+1, e-1)
        else:
            memo[(s,e)] = rec(s+1,e) + rec(s,e-1) - rec(s+1,e-1)
    return memo[(s,e)]

inp = "abdbca"
start = 0
end = len(inp) -1
print(rec(start, end))



