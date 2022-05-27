# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/

def longestCommonPref(strs: List[str]):
    l, r = 0, len(min(strs, key=len)) - 1

    prev = ''
    res = ''
    while (l <= r):
        for i in range(len(strs)):
            if i == 0:
                prev = strs[0][l]
            else:
                if prev != strs[i][l]:
                    return res
        res += prev
        l += 1
    return res
