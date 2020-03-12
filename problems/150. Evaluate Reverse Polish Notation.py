'''
https://leetcode.com/problems/evaluate-reverse-polish-notation/
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
    
    def isEmpty(self) -> bool:
        return not self.data


class Solution:
    def evalRPN(self, tokens: list) -> int:
        result = Stack()
        
        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                result.push(int(token))
            else:
                second = result.pop()
                first = result.pop()
                
                if token == "+": result.append(first + second)
                if token == "-": result.append(first - second)
                if token == "*": result.append(first * second)
                if token == "/": result.append(int(first / second))
        
        return result.peek()