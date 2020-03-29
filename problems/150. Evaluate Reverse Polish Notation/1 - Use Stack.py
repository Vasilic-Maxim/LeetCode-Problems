from collections import deque


class Solution:
    def evalRPN(self, tokens: list) -> int:
        result = deque()

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                result.append(int(token))
            else:
                second = result.pop()
                first = result.pop()

                if token == "+":
                    result.append(first + second)
                if token == "-":
                    result.append(first - second)
                if token == "*":
                    result.append(first * second)
                if token == "/":
                    result.append(int(first / second))

        return result[-1]
