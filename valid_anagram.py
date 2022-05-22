# https://leetcode.com/problems/valid-anagram/

def isAnagram(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False

    s_hash = {}
    t_hash = {}

    for i in range(len(s)):
        s_hash[s[i]] = s_hash.get(s[i], 0) + 1
        t_hash[t[i]] = t_hash.get(t[i], 0) + 1

    if len(s_hash) != len(t_hash):
        return False

    for i in s_hash:
        if s_hash[i] != t_hash.get(i, 0):
            return False
    return True

