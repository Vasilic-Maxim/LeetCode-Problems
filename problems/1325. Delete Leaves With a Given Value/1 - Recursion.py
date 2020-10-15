from typing import Union


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, node: TreeNode, target: int) -> Union[TreeNode, None]:
        """
        Time: O(n)
        Space: O(height)
        """

        if node is None:
            return None

        node.left = self.removeLeafNodes(node.left, target)
        node.right = self.removeLeafNodes(node.right, target)

        if node.left is None and node.right is None:
            return None if node.val == target else node

        return node
