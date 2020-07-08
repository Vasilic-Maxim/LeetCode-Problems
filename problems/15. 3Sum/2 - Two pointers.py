from typing import List


class Solution:
    """
    m - number of possible combinations with sum 0
    Time: O(n ** 2)
    Space: O(m)
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []

        nums.sort()
        result = []
        for i in range(n - 2):
            if i and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, n - 1
            while j < k:
                target = nums[i] + nums[j] + nums[k]
                if not target:
                    result.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif target < 0:
                    j += 1
                else:
                    k -= 1
        return result
