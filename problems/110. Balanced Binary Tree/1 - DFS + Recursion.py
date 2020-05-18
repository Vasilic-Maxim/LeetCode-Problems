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

    def isBalanced(self, node: TreeNode) -> bool:
        return self.get_balance(node)[0]

    def get_balance(self, node: TreeNode) -> tuple:
        l_balance = r_balance = 0

        if node is not None:
            l_is_balanced, l_balance = self.get_balance(node.left)
            if not l_is_balanced:
                return False, 0

            r_is_balanced, r_balance = self.get_balance(node.right)
            if not r_is_balanced:
                return False, 0

        return abs(l_balance - r_balance) <= 1, max(l_balance, r_balance) + 1
