class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    Time: O(n)
    Space: O(n) - call stack
    """

    def __init__(self):
        self.total = 0

    def convertBST(self, node: TreeNode) -> TreeNode:
        if node is not None:
            self.convertBST(node.right)
            self.total += node.val
            node.val = self.total
            self.convertBST(node.left)
        return node
