class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Time/Space: O(n)
    """

    def deepestLeavesSum(self, root):
        previous_lvl = []
        current_lvl = [root]
        while current_lvl:
            previous_lvl = current_lvl
            current_lvl = [child
                           for node in current_lvl
                           for child in [node.left, node.right]
                           if child is not None]
        return sum(node.val for node in previous_lvl)
