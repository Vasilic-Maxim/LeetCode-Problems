from collections import deque


class Solution:
    def isValid(self, s: str):
        if len(s) % 2:
            return False

        brackets = {")": "(", "]": "[", "}": "{"}
        stack = deque()

        for i in s:
            if i in brackets:
                elem = stack.pop()
                if elem != brackets[i]:
                    return False
            else:
                stack.append(i)

        return len(stack)
