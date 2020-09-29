from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Time: O(n ** 2)
    Space: O(n)
    """

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def find_mid(lo: int, hi: int) -> int:
            mid = lo
            for i in range(lo + 1, hi + 1):
                if nums[i] > nums[mid]:
                    mid = i
            return mid

        def construct(lo: int, hi: int):
            if lo >= hi:
                return None

            mid = find_mid(lo, hi)
            return TreeNode(
                nums[mid],
                construct(lo, mid - 1),
                construct(mid + 1, hi)
            )

        return construct(0, len(nums) - 1)
