from typing import List


class Solution:
    """
    Time: O(2 ** n)
    Space: O(n)
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        self.dfs(nums, 0, [], subsets)
        return subsets

    def dfs(self, nums: List[int], index: int, path: List[int], subsets: List[List[int]]):
        if index == len(nums):
            subsets.append(path[:])
            return

        path.append(nums[index])
        self.dfs(nums, index + 1, path, subsets)
        path.pop()
        self.dfs(nums, index + 1, path, subsets)
