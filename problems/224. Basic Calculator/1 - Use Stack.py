import re
from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def calculate(self, s: str) -> int:
        inputs = re.findall(re.compile('(\d+|[^ 0-9])'), s)
        math_operations = {'+', '-', '('}
        operands = []
        operations = []
        for item in inputs:
            if item in math_operations:
                operations.append(item)
            else:
                if item == ')':
                    operations.pop()
                else:
                    operands.append(int(item))

                if operations and operations[-1] != '(':
                    self.calc(operands, operations)

        if operations:
            self.calc(operands, operations)

        return operands.pop()

    def calc(self, operands: List[int], operations: List[str]):
        second = operands.pop()
        first = operands.pop()
        operands.append(first + (second if operations.pop() == "+" else -second))
