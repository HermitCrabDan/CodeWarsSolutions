#https://www.codewars.com/kata/517abf86da9663f1d2000003
def to_camel_case(text):
    r = ""
    for i,l in enumerate(text):
        if i == 0:
            r = l
        elif text[i-1] == "_":
            r = r + l.upper()
        elif text[i-1] == "-":
            r = r + l.upper()
        elif l != "-" and l != "_":
            r = r+ l.lower()
    return r