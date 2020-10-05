class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Time/Space: O(n)
    """

    def findSecondMinimumValue(self, node: TreeNode) -> int:
        if node.left is None and node.right is None:
            return -1

        left = self.findSecondMinimumValue(node.left)
        right = self.findSecondMinimumValue(node.right)
        candidates = [candidate
                      for candidate
                      in [left, right, node.left.val, node.right.val]
                      if candidate > node.val]
        return min(candidates or [0]) or -1
