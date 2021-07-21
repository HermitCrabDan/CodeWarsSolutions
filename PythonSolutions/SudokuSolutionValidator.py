#https://www.codewars.com/kata/529bf0e9bdf7657179000008
def valid_solution(board):
    #print(board)
    n = len(board)
    valid = True
    s = []
    xs = ys = 0
    for i in range(n):
        if i+1 not in board[i]:
            valid = False
            continue
        c = []
        y = 0
        sq = []
        for j in range(n):
            c.append(board[j][i])
            x = j % 3
            if x == 0 and j > 0:
                y += 1
            sq.append(board[ys+y][xs+x])            
        s.append(sq)
        s.append(c)        
        if (i+1) % 3:
            xs += 3
        else:
            ys += 3
            xs = 0
    for e in range(n):
        for a in s:
            if e+1 not in a:
                valid = False
                continue
    #print(valid)
    return valid