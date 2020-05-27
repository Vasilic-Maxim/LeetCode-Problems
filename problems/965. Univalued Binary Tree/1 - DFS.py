class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, node: TreeNode) -> bool:
        left = node.left is None or (node.left.val == node.val and self.isUnivalTree(node.left))
        right = node.right is None or (node.right.val == node.val and self.isUnivalTree(node.right))
        return left and right
