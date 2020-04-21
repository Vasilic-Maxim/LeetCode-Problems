from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def repeatedNTimes(self, nums: List[int]) -> int:
        visited = set()
        for num in nums:
            if num in visited:
                return num
            visited.add(num)
