# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/

def firstUniqueChar(s: str) -> int:
    d = {}

    for c in s:
        d[c] = 1 + d.get(c, 0)

    for k in d:
        if d[k] == 1:
            return s.find(k)
    return -1
