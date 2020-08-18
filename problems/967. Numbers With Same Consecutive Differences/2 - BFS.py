from collections import deque
from typing import List


class Solution:
    """
    Time: O(n * 2 ** n)
    Space: O(2 ** n)
    """

    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return [i for i in range(10)]

        result = []
        queue = deque([(n - 1, num) for num in range(1, 10)])

        while queue:
            level, combination = queue.pop()

            if level == 0:
                result.append(combination)
            else:
                last_digit = combination % 10
                next_digits = {last_digit - k, last_digit + k}
                combination *= 10
                for next_digit in next_digits:
                    if 0 <= next_digit < 10:
                        queue.appendleft((level - 1, combination + next_digit))

        return result
