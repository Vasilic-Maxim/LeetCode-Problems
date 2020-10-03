class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def flatten(self, root: TreeNode) -> None:
        if root is not None:
            self.dfs(root)

    def dfs(self, node: TreeNode) -> TreeNode:
        if node.left is not None and node.right is not None:
            left_leaf = self.dfs(node.left)
            right_leaf = self.dfs(node.right)
            left_leaf.right = node.right
            node.right, node.left = node.left, None
            return right_leaf

        if node.left is not None:
            node.right, node.left = node.left, None
            return self.dfs(node.right)

        if node.right is not None:
            return self.dfs(node.right)

        return node
