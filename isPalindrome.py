# https://leetcode.com/problems/valid-palindrome/

def isPalindrome(s: str) -> bool:
    new_s = [i.lower() for i in s if i.isalnum()]

    l, r = 0, len(new_s) -1
    while (l < r):
        if new_s[l] != new_s[r]:
            return False
        l +=1
        r -= 1
    return True

