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
        stack = [root]
        while stack:
            node = stack.pop()
            if node is not None:
                node.left, node.right = node.right, node.left
                stack.extend([node.left, node.right])

        return root
