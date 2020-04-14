class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """
    def __init__(self):
        self.tree_tilt = 0

    def findTilt(self, root: TreeNode) -> int:
        self.calcTreeSum(root)
        return self.tree_tilt

    def calcTreeSum(self, root: TreeNode) -> int:
        if root is None:
            return 0

        left = self.calcTreeSum(root.left)
        right = self.calcTreeSum(root.right)
        self.tree_tilt += abs(left - right)
        return left + right
