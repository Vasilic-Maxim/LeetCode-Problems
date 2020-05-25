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

    def rangeSumBST(self, root: TreeNode, left: int, right: int) -> int:
        result = 0
        if root is not None:
            if left <= root.val <= right:
                result = root.val

            if left < root.val:
                result += self.rangeSumBST(root.left, left, right)
            if right > root.val:
                result += self.rangeSumBST(root.right, left, right)
        return result
