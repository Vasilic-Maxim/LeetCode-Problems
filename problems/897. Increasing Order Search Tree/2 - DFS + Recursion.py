class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    TIme: O(n)
    Space: O(n)
    """

    def __init__(self):
        self.root = None
        self.tail = None

    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.dfs(root)
        return self.root

    def dfs(self, node: TreeNode) -> None:
        if node.left is not None:
            tmp, node.left = node.left, None
            self.dfs(tmp)

        if self.root is not None:
            self.tail.right = node
            self.tail = self.tail.right
        else:
            self.root = self.tail = node

        if node.right is not None:
            self.dfs(node.right)
