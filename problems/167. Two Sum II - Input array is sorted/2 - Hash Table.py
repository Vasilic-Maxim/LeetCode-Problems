class Solution:
    """
    Time: O(n)
    Space: O(n) - for hash-table
    """

    def twoSum(self, nums: list, target: int) -> list:
        data = {}
        for i, val in enumerate(nums):
            if target - val in data:
                return [data[target - val] + 1, i + 1]

            if val not in data:
                data[val] = i
