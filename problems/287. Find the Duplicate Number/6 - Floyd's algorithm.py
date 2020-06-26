from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = hare = nums[0]
        while 1:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare
