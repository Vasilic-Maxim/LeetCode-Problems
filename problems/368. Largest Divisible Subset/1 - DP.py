from typing import List


class Solution:
    """
    Explanation:
    https://leetcode.com/problems/largest-divisible-subset/discuss/684740
    https://leetcode.com/problems/largest-divisible-subset/discuss/684738
    https://leetcode.com/problems/largest-divisible-subset/discuss/193011
    https://leetcode.com/problems/largest-divisible-subset/discuss/84002/
    Time: O(n ** 2)
    Space: O(n)
    """

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # Return empty list if 'nums' is empty
        if not nums:
            return []

        # Sort the initial list
        nums.sort()
        count = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if not nums[i] % nums[j]:
                    count[i] = max(count[i], count[j] + 1)

        max_index = max(range(len(count)), key=count.__getitem__)

        result = []
        temp = nums[max_index]
        current_count = count[max_index]
        for i in range(max_index, -1, -1):
            if not temp % nums[i] and current_count == count[i]:
                result.append(nums[i])
                temp = nums[i]
                current_count -= 1
        return result
