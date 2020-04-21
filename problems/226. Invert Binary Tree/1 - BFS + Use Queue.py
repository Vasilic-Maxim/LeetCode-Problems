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
        q = deque([root])
        while len(q):
            node = q.popleft()
            if node is not None:
                node.left, node.right = node.right, node.left
                q.extend([node.left, node.right])

        return root
