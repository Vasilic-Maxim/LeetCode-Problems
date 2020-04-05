class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, path_sum: int) -> bool:
        if root is None:
            return False

        if root.left is None and root.right is None:
            return path_sum == root.val

        if root.left is not None:
            if self.hasPathSum(root.left, path_sum - root.val):
                return True

        return self.hasPathSum(root.right, path_sum - root.val)
