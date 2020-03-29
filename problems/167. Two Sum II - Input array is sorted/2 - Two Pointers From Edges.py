class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def twoSum(self, nums: list, target: int) -> list:
        current = 0
        last = len(nums) - 1
        while True:
            if nums[current] + nums[last] > target:
                last -= 1
            elif nums[current] + nums[last] < target:
                current += 1
            else:
                return [current + 1, last + 1]
