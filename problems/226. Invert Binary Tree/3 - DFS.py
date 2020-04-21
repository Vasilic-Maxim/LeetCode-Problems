from collections import deque
from typing import Optional


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
    def invertTree(self, root: TreeNode) -> Optional[TreeNode]:
        if root is not None:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root
