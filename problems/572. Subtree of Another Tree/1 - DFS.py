class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, first: TreeNode, second: TreeNode):
        if first is None:
            return False
        if self.is_match(first, second):
            return True
        return self.isSubtree(first.left, second) or self.isSubtree(first.right, second)

    def is_match(self, first: TreeNode, second: TreeNode) -> bool:
        if first is None and second is None:
            return True
        if first is None or second is None:
            return False

        return (first.val == second.val and
                self.is_match(first.left, second.left) and
                self.is_match(first.right, second.right))
