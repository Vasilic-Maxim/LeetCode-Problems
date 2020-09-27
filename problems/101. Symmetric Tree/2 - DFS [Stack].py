class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def isSymmetric(self, root: TreeNode) -> bool:
        stack = [root, root]
        while stack:
            left, right = stack.pop(), stack.pop()

            if left is None and right is None:
                continue

            if left is None or right is None:
                return False

            if left.val != right.val:
                return False

            stack.extend([left.left, right.right, left.right, right.left])

        return True
