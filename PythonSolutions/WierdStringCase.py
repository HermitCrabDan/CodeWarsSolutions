#https://www.codewars.com/kata/52b757663a95b11b3d00062d
def to_weird_case(string):
    r = ""
    i = 0
    for l in string:
        if l == " ":
            r += l
            i = 0
        elif i % 2 == 0:
            r += l.upper()
            i += 1
        else:
            r = r + l.lower()
            i += 1
    return r