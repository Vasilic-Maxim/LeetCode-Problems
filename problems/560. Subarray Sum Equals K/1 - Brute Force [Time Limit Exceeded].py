from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = 0
        for i in range(len(nums)):
            count = 0
            for _, num in enumerate(nums[i:]):
                count += num
                if count == k:
                    counter += 1

        return counter
