#https://www.codewars.com/kata/52e88b39ffb6ac53a400022e
def int32_to_ip(i):
    return '.'.join([str(x) for x in [i >> 24, i >> 16 & 0xFF, i >> 8 & 0xFF, i & 0xFF]])

#previous Solution
def int32_to_ipPrevious(int32):
    # your code here
    x1 = int32 >> 24
    int32 = int32 - (x1 << 24)
    x2 = int32 >> 16
    int32 = int32 - (x2 << 16)
    x3 = int32 >> 8
    int32 = int32 - (x3 << 8)
    x4 = int32
    return str(x1) + "." + str(x2) + "." + str(x3) + "." + str(x4)