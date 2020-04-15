from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def __init__(self):
        self.current_path = []
        self.paths = []

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is not None:
            self.scanPaths(root)

        return self.paths

    def scanPaths(self, node: TreeNode):
        self.current_path.append(str(node.val))

        if node.left is None and node.right is None:
            self.paths.append("->".join(self.current_path))
        else:
            if node.left is not None:
                self.binaryTreePaths(node.left)

            if node.right is not None:
                self.binaryTreePaths(node.right)

        self.current_path.pop()
