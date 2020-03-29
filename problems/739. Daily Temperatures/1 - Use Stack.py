from collections import deque


class Solution:
    def dailyTemperatures(self, temperatures: list) -> list:
        stack = deque()
        result = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            while len(stack) and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            if len(stack):
                result[i] = stack[-1] - i

            stack.append(i)
        return result
