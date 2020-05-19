class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    ==== Balanced BST ====
    Time: O(log (n))
    Space: O(log (n))

    ==== Unbalanced BST ====
    Time: O(n)
    Space: O(n)
    """

    def lowestCommonAncestor(self, node: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if max(p.val, q.val) < node.val:
            return self.lowestCommonAncestor(node.left, p, q)
        elif min(p.val, q.val) > node.val:
            return self.lowestCommonAncestor(node.right, p, q)
        return node
