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

        def DFS(level, combination):
            if level == 0:
                return result.append(combination)

            last_digit = combination % 10
            next_digits = {last_digit - k, last_digit + k}
            combination *= 10
            for next_digit in next_digits:
                if 0 <= next_digit < 10:
                    DFS(level - 1, combination + next_digit)

        for num in range(1, 10):
            DFS(n - 1, num)

        return result
