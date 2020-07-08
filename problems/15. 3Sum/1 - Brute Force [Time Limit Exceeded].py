import bisect
from typing import List


class Solution:
    """
    Brute Force evolution:
        1. Three loops - Time: O(n ** 3)
        2, Two loops + binary search - O(n ** 2 * log (n))

    m - number of possible combinations with sum 0
    Space: O(m)
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = set()
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                wanted = 0 - nums[i] - nums[j]
                index = bisect.bisect_left(nums, wanted, j + 1, n - 1)
                if index < n and nums[index] == wanted:
                    result.add((nums[i], nums[j], nums[index]))
        return list(map(list, result))
