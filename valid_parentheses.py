# https://leetcode.com/problems/valid-parentheses/

# [(] is false

def isValid(s: str) -> bool:
    stack = []
    closers = {')': '(', ']': '[', '}': '{'}
    for i in s:
        if i in closers:
            if len(stack) == 0:
                return False
            v = stack.pop()
            if v != closers.get(i, ''):
                return False
        else:
            stack.append(i)
    
    if len(stack) > 0:
        return False
    return True

