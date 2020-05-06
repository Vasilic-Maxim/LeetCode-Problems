class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, first: TreeNode, second: TreeNode) -> bool:
        if first is None or second is None:
            return first is second

        if first.val == second.val:
            return self.isSameTree(first.left, second.left) and self.isSameTree(first.right, second.right)

        return False
