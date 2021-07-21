#https://www.codewars.com/kata/52bc74d4ac05d0945d00054e
def first_non_repeating_letter(string):
    s = string.lower()
    i = 0
    while i < len(s):
        c = s[i]
        if s.find(c,i+1) == -1 and s.find(c,0,i) == -1:
            return string[i]
        i += 1
    return ""