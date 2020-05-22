class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    ===== Unbalanced BST =====
    Time: O(n)
    Space: O(n)

    ===== Balanced BST =====
    Time: O(n)
    Space: O(log (n))
    """

    def sumOfLeftLeaves(self, node: TreeNode, is_left: bool = False) -> int:
        if node is None:
            return 0

        if node.left is None and node.right is None and is_left:
            return node.val

        return self.sumOfLeftLeaves(node.left, True) + self.sumOfLeftLeaves(node.right, False)
