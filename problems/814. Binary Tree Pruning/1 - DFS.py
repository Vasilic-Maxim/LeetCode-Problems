from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, node: TreeNode):
        """
        Time: O(n)
        Space: O(log (n)) or O(n)
        """

        if node is None:
            return None

        node.left = self.pruneTree(node.left)
        node.right = self.pruneTree(node.right)

        if node.val == 0 and node.left is None and node.right is None:
            return None

        return node
