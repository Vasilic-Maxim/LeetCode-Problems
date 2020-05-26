class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, node: TreeNode, val: int):
        if node is not None and node.val != val:
            return self.searchBST(node.left if node.val > val else node.right, val)
        return node
