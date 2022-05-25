# https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:

        min_val = self.stack[0]
        l, r = 1, len(self.stack) -1
        while(l <= r):
            if min_val > self.stack[l]:
                min_val = self.stack[l]
            if min_val > self.stack[r]:
                min_val = self.stack[r]
            l +=1
            r -=1
        return min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



