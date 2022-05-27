# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/

def reverseInteger(x: int) -> int:
    MAX_constraint = 2**31 - 1
    MIN_constraint = -2**31

    s = str(x)
    y = ''
    res = 0
    for i in range(len(s) - 1, 0, -1):
        y += s[i]

    if s[0] == '-':
        res = -(int(y))
    else:
        y += s[0]
        res = int(y)
    if res < MIN_constraint or res > MAX_constraint:
        return 0
    return res
