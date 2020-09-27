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
        def traverse(left: TreeNode, right: TreeNode) -> bool:
            if left is None or right is None:
                return left is right

            return (
                left.val == right.val and
                traverse(left.left, right.right) and
                traverse(left.right, right.left)
            )

        return traverse(root, root)
