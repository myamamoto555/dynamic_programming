def rec(s, e):
    if s > e:
        return 0
    if s == e:
        return 1
    c1 = 0
    if inp[s] == inp[e]:
        remain = e - s - 1
        if remain == rec(s+1,e-1):
            c1 = 2 + remain
    c2 = rec(s+1,e)
    c3 = rec(s,e-1)
    return max(c1,c2,c3)


inp = "abdbca"
start = 0
end = len(inp) -1
print (rec(start, end))


