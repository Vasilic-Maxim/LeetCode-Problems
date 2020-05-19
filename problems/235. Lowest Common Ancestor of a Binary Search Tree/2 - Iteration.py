class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    ==== Balanced BST ====
    Time: O(log (n))
    Space: O(1)

    ==== Unbalanced BST ====
    Time: O(n)
    Space: O(1)
    """
    def lowestCommonAncestor(self, node: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lo, hi = sorted([p.val, q.val])
        while hi < node.val or lo > node.val:
            node = (node.left, node.right)[lo > node.val]
        return node
