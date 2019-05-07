def rec(s1, e1, s2, e2, count):
    if s1 == e1 or s2 == e2:
        return count

    if st1[s1] == st2[s2]:
        count = rec(s1+1, e1, s2+1, e2, count+1)
    c1 = rec(s1+1, e1, s2, e2, 0)
    c2 = rec(s1+1, e1, s2+1, e2, 0)
    return max(c1,c2,count)

st1 = 'abdca'
st2 = 'cbda'

#memo = [[[None] * len(st2)] *len(st1)] * len(st2)
#print(memo)

print(rec(0, len(st1)-1, 0, len(st2)-1, 0))
#print(memo)
