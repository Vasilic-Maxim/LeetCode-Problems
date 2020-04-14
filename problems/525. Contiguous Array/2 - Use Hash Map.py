from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def findMaxLength(self, nums: List[int]) -> int:
        data = {0: -1}
        count = max_len = 0
        for i, val in enumerate(nums):
            count += 1 if val else -1
            if count in data:
                max_len = max(max_len, i - data[count])
            else:
                data[count] = i
        return max_len
