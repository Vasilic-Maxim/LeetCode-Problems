class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Time: O(n)
    Space (unbalanced tree): O(n)
    Space (balanced tree): O(log (n))
    """

    def sumNumbers(self, node: TreeNode, path: int = 0) -> int:
        if node is None:
            return 0

        path = path * 10 + node.val

        if node.left is None and node.right is None:
            return path

        return self.sumNumbers(node.left, path) + self.sumNumbers(node.right, path)
