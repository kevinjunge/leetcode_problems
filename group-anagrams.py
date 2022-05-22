# https://leetcode.com/problems/group-anagrams/

def groupAnagrams(strs: List[str]) -> List[List[str]]:

    res = []
    d = {}
    for i in strs:
        s = ''.join(sorted(i)) 
        if s not in d:
            d[s] = [i]
        else:
            d[s].append(i)

    for k in d:
        res.append(d[k])

    if len(res) == 0:
        return [[]]

    return res

