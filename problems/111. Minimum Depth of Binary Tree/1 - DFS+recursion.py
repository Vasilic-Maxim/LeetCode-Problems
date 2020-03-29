class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    n - total number of nodes in tree
    Time: O(n)
    Space: O(log n) - call stack
    """

    def minDepth(self, root: TreeNode, depth: int = 0) -> int:
        if root is None:
            return depth

        depth += 1

        if root.left is None and root.right is None:
            return depth

        left = self.minDepth(root.left, depth) if root.left is not None else float('inf')
        right = self.minDepth(root.right, depth) if root.right is not None else float('inf')
        return min(left, right)
