class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_path = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.traverse(root)
        return self.max_path

    def traverse(self, node: TreeNode, prev: int = None) -> int:
        if node is None:
            return 0

        left = self.traverse(node.left, node.val)
        right = self.traverse(node.right, node.val)
        self.max_path = max(self.max_path, left + right)
        return max(left, right) + 1 if node.val == prev else 0
