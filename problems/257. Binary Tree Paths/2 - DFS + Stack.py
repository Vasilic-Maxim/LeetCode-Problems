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

    def binaryTreePaths(self, node: TreeNode) -> List[str]:
        paths, stack = [], [(node, "")]

        if node is not None:
            while stack:
                node, path = stack.pop()
                if node.left is None and node.right is None:
                    paths.append(f"{path}{node.val}")
                if node.right is not None:
                    stack.append((node.right, f"{path}{node.val}->"))
                if node.left is not None:
                    stack.append((node.left, f"{path}{node.val}->"))

        return paths
