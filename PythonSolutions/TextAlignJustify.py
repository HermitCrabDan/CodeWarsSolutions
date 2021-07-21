#https://www.codewars.com/kata/537e18b6147aa838f600001b
def justify(text, width):
    ret = ""
    s = text.split()
    i = 0
    while i < len(s):
        l = 0
        t = []
        while l < width:
            if i < len(s) and (l + len(s[i]) + len(t)) <= width:
                t.append(s[i])
                l += len(s[i])
                i += 1
            else:
                df = width - l
                if len(t) == 1 or i == len(s) or df == len(t)-1:
                    ret += ' '.join(t)
                else:
                    tsp = []
                    for ts in range(len(t)-1):
                        tsp.append(1)
                        df -= 1
                    while df > 0:
                        ti = 0
                        while ti < len(tsp):
                            if (df > 0):
                                tsp[ti] += 1
                                df -= 1
                            ti += 1
                    j = 0
                    while j < len(t):
                        if j == 0:
                            ret += t[j]
                        else:
                            ret += ''.join(' ' for sp in range(tsp[j-1])) + t[j]
                        j += 1
                if i < len(s):
                    ret += '\n'
                l = width
    return ret

#Previous Solution
def justifyPreviousSolution(text, width):
    ret = ""
    s = text.split()
    i = 0
    while i < len(s):
        l = 0
        t = []
        while l < width:
            if i < len(s) and (l + len(s[i]) + len(t)) <= width:
                t.append(s[i])
                l += len(s[i])
                i += 1
            else:
                df = width - l
                if i == len(s) or df == len(t)-1:
                    ret += ' '.join(t)
                elif len(t) == 1:
                    ret += t[0]
                elif len(t) == 2:
                    ret += t[0] + ''.join(' ' for x in range(df)) + t[1]
                else:
                    tsp = []
                    for ts in range(len(t)-1):
                        tsp.append(1)
                        df -= 1
                    #need to balance the spaces
                    while df > 0:
                        ti = 0
                        while ti < len(tsp):
                            if (df > 0):
                                tsp[ti] += 1
                                df -= 1
                            ti += 1
                    j = 0
                    while j < len(t):
                        if j == 0:
                            ret += t[j]
                        else:
                            ret += ''.join(' ' for sp in range(tsp[j-1])) + t[j]
                        j += 1
                if i < len(s):
                    ret += '\n'
                l = width
    return ret