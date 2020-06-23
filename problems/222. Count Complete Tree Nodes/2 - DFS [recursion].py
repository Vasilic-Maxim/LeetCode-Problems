class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Recursive solution is quiet simple, doesn't it?
    Even though we improved the space complexity we
    definitely do not take all potential of the fact
    that the tree is complete (or perfect).

    Time: O(n)
    Space: O(log (n))
    """

    def countNodes(self, node: TreeNode) -> int:
        if node is None:
            return 0
        return 1 + self.countNodes(node.left) + self.countNodes(node.right)
