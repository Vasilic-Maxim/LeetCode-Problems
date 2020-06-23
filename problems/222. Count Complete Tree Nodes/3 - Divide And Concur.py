class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    The idea of this approach is to find perfect trees
    because for the perfect binary tree there is the
    formula that permits us to compute number of nodes
    in the tree.

    Time: O(log (n) * log (n))
    Space: O(log (n))
    """

    def countNodes(self, node: TreeNode) -> int:
        if node is None:
            return 0

        left_height = self.height(node.left)
        right_height = self.height(node.right)
        if left_height == right_height:
            # Perfect binary tree is detected
            return 2 ** left_height + self.countNodes(node.right)
        # If heights differ than it means that the right side
        # is a perfect tree and the left side contains a
        # doorstep. We can relay on that observation because
        # by definition the tree is complete that means that
        # each level is filled from left to right.
        return 2 ** right_height + self.countNodes(node.left)

    def height(self, node: TreeNode) -> int:
        if node is None:
            return 0
        return 1 + self.height(node.left)
