'''
https://leetcode.com/problems/daily-temperatures/
'''

class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, x) -> None:
        self.data.append(x)
    
    def pop(self):
        if not self.isEmpty():
            return self.data.pop()
    
    def peek(self):
        if not self.isEmpty():
            return self.data[-1]
    
    def isEmpty(self):
        return not self.data

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = Stack()
        result = [0] * len(T)
        
        for i in range(len(T)-1,-1,-1):
            while not stack.isEmpty() and T[stack.peek()] <= T[i]:
                stack.pop()
            
            if not stack.isEmpty():
                result[i] = stack.peek() - i
            
            stack.push(i)
        return result