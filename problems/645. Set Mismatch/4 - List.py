from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def findErrorNums(self, nums: List[int]) -> List[int]:
        appearance = [0] * (len(nums) + 1)
        for num in nums:
            appearance[num] += 1

        dup = missing = None
        for i in range(1, len(appearance)):
            if not appearance[i]:
                missing = i
            elif appearance[i] == 2:
                dup = i

        return [dup, missing]
