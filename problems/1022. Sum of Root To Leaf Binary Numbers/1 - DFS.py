class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.sum = 0

    def sumRootToLeaf(self, root: TreeNode) -> int:
        if root is not None:
            self.dfs(root, 0)
        return self.sum

    def dfs(self, node: TreeNode, path_sum: int):
        path_sum = path_sum * 2 + node.val

        if node.left is None and node.right is None:
            self.sum += path_sum
        else:
            if node.left is not None:
                self.dfs(node.left, path_sum)
            if node.right is not None:
                self.dfs(node.right, path_sum)
