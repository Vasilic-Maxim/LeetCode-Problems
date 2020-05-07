class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def trimBST(self, node: TreeNode, left: int, right: int) -> TreeNode:
        if node is not None:
            if node.val < left:
                return self.trimBST(node.right, left, right)
            if node.val > right:
                return self.trimBST(node.left, left, right)

            node.left = self.trimBST(node.left, left, right)
            node.right = self.trimBST(node.right, left, right)

        return node
