from typing import List


class Solution:
    """
    Time: O(n ** 2)
    Space: O(1)
    """

    def checkIfExist(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            mul = nums[i] * 2
            div, mod = divmod(nums[i], 2)
            for j in range(i + 1, len(nums)):
                if i == j:
                    continue

                if mul == nums[j]:
                    return True

                if not mod and div == nums[j]:
                    return True

        return False
