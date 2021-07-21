#https://www.codewars.com/kata/52756e5ad454534f220001ef
def lcs(x, y):
    if not x or not y: return ""
    if x[0] == y[0]: return x[0] + lcs(x[1:], y[1:])
    
    return max(lcs(x[1:], y), lcs(x, y[1:]), key=len)

#previous solution
def lcsPrevious(x, y):
    d = {}
    d.update(cs(x,y))
    d.update(cs(y,x))
    return max(d.keys(), key =lambda k:d[k] )
def cs(s1,s2):
    td = {}
    ti = 0
    while ti < len(s1):
        r = []
        z = 0
        for j in s1[ti:]:
            t = s2.find(j,z,)
            if t !=-1:
                r.append(j)
                z = t+1
        td[''.join(r)] = len(r)
        ti += 1
    return td