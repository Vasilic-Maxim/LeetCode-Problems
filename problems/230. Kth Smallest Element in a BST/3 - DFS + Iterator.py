import itertools


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Note:
    You pay "k" for "pop"-ing elements from the stack

    ====== Unbalanced Tree (all nodes on the left side) =====
    Time: O(n + k)
    Space: O(n)

    ====== Balanced Tree =====
    Time: O(log (n) + k)
    Space: O(n)
    """

    def kthSmallest(self, node: TreeNode, k: int) -> int:
        # do exactly one step
        return next(itertools.islice(self.inorder(node), k - 1, k))

    def inorder(self, node: TreeNode):
        if node:
            yield from self.inorder(node.left)
            yield node.val
            yield from self.inorder(node.right)
