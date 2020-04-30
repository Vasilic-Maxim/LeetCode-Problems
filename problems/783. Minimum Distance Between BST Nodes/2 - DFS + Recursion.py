import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def __init__(self):
        self.min_diff = sys.maxsize
        self.prev = ~sys.maxsize

    def minDiffInBST(self, node: TreeNode) -> int:
        if node.left is not None:
            self.minDiffInBST(node.left)

        self.min_diff = min(self.min_diff, node.val - self.prev)
        self.prev = node.val

        if node.right is not None:
            self.minDiffInBST(node.right)

        return self.min_diff
