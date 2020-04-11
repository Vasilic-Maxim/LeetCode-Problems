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
        self.diameter: int = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0

        self.maxPath(root)
        return self.diameter

    def maxPath(self, node: TreeNode) -> int:
        if node is None:
            return 0

        left = self.maxPath(node.left)
        right = self.maxPath(node.right)
        self.diameter = max(self.diameter, left + right)

        return max(left, right) + 1
