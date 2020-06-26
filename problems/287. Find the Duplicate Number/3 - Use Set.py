from typing import List


class Solution:
    """
    NOTE:
        You must use only constant, O(1) extra space.

    Even thought the solution works well we exceed the
    space constrains.

    Time: O(n)
    Space: O(n)
    """

    def findDuplicate(self, nums: List[int]) -> int:
        visited = set()
        for num in nums:
            if num in visited:
                return num

            visited.add(num)
