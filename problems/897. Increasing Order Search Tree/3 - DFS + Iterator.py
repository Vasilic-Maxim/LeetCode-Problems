class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def increasingBST(self, root):
        new_root = tail = TreeNode(None)
        for node in self.in_order(root):
            tail.right = node
            tail = tail.right
        return new_root.right

    def in_order(self, node):
        if node:
            left, right = node.left, node.right
            node.left = node.right = None
            yield from self.in_order(left)
            yield node
            yield from self.in_order(right)
