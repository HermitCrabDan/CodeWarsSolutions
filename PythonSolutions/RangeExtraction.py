#https://www.codewars.com/kata/51ba717bb08c1cd60f00002f
def solution(args):
    ret = []
    v1 = v2 = args[0]
    for n in args[1:] + [""]:
        if n != v2 + 1:
            if v1 == v2:
                ret.append(str(v1))
            elif v2 == v1 + 1:
                ret.extend([str(v1),str(v2)])
            else:
                ret.append(str(v1) + "-" + str(v2))
            v1 = n
        v2 = n
        
    return ",".join(ret)

#previous Solution
def solutionPrevious(args):
    v1 = args[0]
    v2 = v1
    i = 1
    ret = ""
    seq = 0
    while i < len(args):
        if v2 + 1 == args[i]:
            if seq == 0:
                v1 = v2
            seq = seq + 1
        else:
            if seq >= 2:
                ret = ret + "," + str(v1) + "-" + str(v2)
            elif seq == 1:
                ret = ret + "," + str(v1) + "," + str(v2)
            else:
                ret = ret + "," + str(v2)
            seq = 0
        v2 = args[i]
        i = i+1
    
    if seq >= 2:
        ret = ret + "," + str(v1) + "-" + str(v2)
    elif seq == 1:
        ret = ret + "," + str(v1) + "," + str(v2)
    else:
        ret = ret + "," + str(v2) 
    
    return str(ret[1:])