#https://www.codewars.com/kata/52423db9add6f6fc39000354
from copy import deepcopy
def get_generation(cells, generations): 
    r = deepcopy(cells)
    while generations > 0 and len(r) > 0:    
        for n in range(len(r)):
            r[n].insert(0,0)
            r[n].append(0)
        if len(r) > 0:
            a = [0] * len(r[0])
            b = [0] * len(r[0])
            r.insert(0,a)
            r.append(b)
        c = deepcopy(r)
        for x in range(len(r)):
            for y in range(len(r[0])):
                cell = r[x][y]
                neighbors = live_area(c, x, y) - cell
                if cell:
                    if neighbors > 3:
                        r[x][y] = 0
                    elif neighbors < 2:
                        r[x][y] = 0
                elif neighbors == 3:
                    r[x][y] = 1
        r = crop_area(r)
        generations -= 1
    return r

def crop_area(matrix):
    crop = True
    while crop == True and len(matrix) > 0:
        t = sum(matrix[0])
        b = sum(matrix[len(matrix)-1])
        le = ri = 0        
        for m in matrix:
            if len(m) > 0:
                le += m[0]
                ri += m[len(m)-1]
        if t and b and le and ri:
            crop = False
        else:
            for n in range(len(matrix)):
                if le == 0 and len(matrix[n]) > 0:
                    matrix[n].pop(0)
                if ri == 0 and len(matrix[n]) > 0:
                    matrix[n].pop()
            if t == 0 and len(matrix) > 0:
                matrix.pop(0)
            elif b == 0 and len(matrix) > 0:
                matrix.pop()         
    return matrix
        
def live_area(c, x, y):
    ret = 0
    for i in range(x - 1 if x > 0 else x, x + 2 if x < len(c)-1 else x+1):
        for j in range(y - 1 if y > 0 else y, y + 2 if y < len(c[0])-1 else y+1):
            ret += c[i][j]
    return ret