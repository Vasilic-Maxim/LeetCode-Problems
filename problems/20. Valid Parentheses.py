'''
https://leetcode.com/problems/valid-parentheses/
'''

class Stack:
    def __init__(self):
        self.data = []
    
    def pop(self):
        if self.data:
            return self.data.pop()

    def push(self, x):
        self.data.append(x)

    def peek(self):
        if self.data:
            return self.data[-1]

    def isEmpty(self):
        return not self.data


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        
        brackets = {")": "(", "]": "[", "}": "{"}
        stack = Stack()
        
        for i in s:
            if i in brackets:
                elem = stack.pop()
                if elem != brackets[i]:
                    return False
            else:
                stack.push(i)
        
        return stack.isEmpty()