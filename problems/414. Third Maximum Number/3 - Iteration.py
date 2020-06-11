import sys
from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(3) => O(1)
    """

    def thirdMax(self, nums: List[int]) -> int:
        result = [-sys.maxsize] * 3
        for num in nums:
            if num in result:
                continue
            for i in range(3):
                if num > result[i]:
                    result[i], num = num, result[i]

        return max(result) if result[-1] == -sys.maxsize else min(result)
