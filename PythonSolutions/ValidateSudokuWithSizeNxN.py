#https://www.codewars.com/kata/540afbe2dc9f615d5e000425
import math
class Sudoku(object):
    def __init__(self, data):
        self.matrix = data
    def is_valid(self):
        n = len(self.matrix)
        r = math.sqrt(n)
        valid = r.is_integer()
        r = int(r)
        if valid == True:
            for i in range(n):                
                if len(self.matrix[i]) != n:
                    valid = False
                if i+1 not in self.matrix[i]:
                    valid = False
        s = []
        if valid == True:
            xs = 0
            ys = 0
            for b in range(n):
                y = 0
                sq = []
                for j in range(n):
                    x = j % r
                    if x == 0 and j > 0:
                        y += 1
                    if type(self.matrix[ys+y][xs+x]) == int:
                        sq.append(self.matrix[ys+y][xs+x])
                    else:
                        valid = False
                        continue
                s.append(sq)                
                if (b+1) % r == 0:
                    ys += r
                    xs = 0
                else:
                    xs += r
            for e in range(n):
                for a in s:
                    if e+1 not in a:
                        valid = False
        return valid