from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def divisorGame(self, num: int) -> bool:
        result: List[bool] = [False] * (num + 1)
        for i in range(1, num + 1):
            for j in range(1, i // 2 + 1):
                if i % j == 0 and not result[i - j]:
                    result[i] = True
                    break
        return result[num]
