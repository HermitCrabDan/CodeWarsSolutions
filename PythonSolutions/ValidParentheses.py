#https://www.codewars.com/kata/52774a314c2333f0a7000688
def valid_parentheses(string):
    l = string.rfind("(")
    if l == -1 and string.find(")") > -1:
        return False
    while l > -1:
        r = string.find(")", l)
        if r == -1:
            return False
        string = string[:l]+string[r+1:]
        l = string.rfind("(")
    if string.find(")") > -1:
        return False
    else:
        return True