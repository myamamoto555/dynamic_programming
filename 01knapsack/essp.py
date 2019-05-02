def get_partition(inp):
    sum = 0
    for i in inp:
        sum += i
    if sum %2 != 0:
        return False
    else:
        return rec(sum/2, 0)

def rec(tgt, i):
    if i >= len(inp):
        return False
    if tgt == 0:
        return True
    if tgt - inp[i] >= 0:
        if rec(tgt - inp[i], i+1):
            return True
    return rec(tgt, i+1)


inp = [1, 2, 3, 4]
print(get_partition(inp))
