'''
https://leetcode.com/problems/min-stack/
'''

class MinStack:

    def __init__(self):
        self.data = []

    def push(self, x: int) -> None:
        if self.data:
            self.data.append((x, min(self.data[-1][1], x)))
        else:
            self.data.append((x, x))

    def pop(self) -> None:
        if self.data:
            self.data.pop()

    def top(self) -> int:
        if self.data:
            return self.data[-1][0]

    def getMin(self) -> int:
        if self.data:
            return self.data[-1][1]