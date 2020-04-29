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
        self.max_path_sum = ~sys.maxsize

    def maxPathSum(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.max_path_sum

    def dfs(self, node: TreeNode) -> int:
        if node is None:
            return 0

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        self.max_path_sum = max(self.max_path_sum, left + right + node.val)

        return max(max(left, right) + node.val, 0)
