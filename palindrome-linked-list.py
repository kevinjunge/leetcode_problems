# https://leetcode.com/problems/palindrome-linked-list/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def isPalindrome(head: Optional[ListNode]):
    stack = []

    while(head):
        stack.append(head.val)
        head = head.next

    l, r = 0, len(stack)-1
    while(l < r):
        if stack[l] != stack[r]:
            return False
        l +=1
        r -=1
    return True

    
