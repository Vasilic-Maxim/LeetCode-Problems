class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.recalculate(root)
        return root

    def recalculate(self, node: TreeNode, value: int = 0):
        if node is None:
            return value

        value = self.recalculate(node.right, value)
        node.val += value

        return self.recalculate(node.left, node.val)
