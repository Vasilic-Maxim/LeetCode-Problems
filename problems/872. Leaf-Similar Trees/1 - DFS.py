from itertools import zip_longest
from operator import eq


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    m - len(root1)
    n - len(root2)
    Time: O(m + n)
    Space (Balanced): O(log (m) + log (n))
    Space (Unbalanced): O(m + n)
    """

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leafs = self.leafs(root1), self.leafs(root2)
        return all(iter(eq(*pair) for pair in zip_longest(*leafs)))

    def leafs(self, tree: TreeNode):
        if tree is not None:
            if tree.left is None and tree.right is None:
                yield tree.val
            else:
                yield from self.leafs(tree.left)
                yield from self.leafs(tree.right)
