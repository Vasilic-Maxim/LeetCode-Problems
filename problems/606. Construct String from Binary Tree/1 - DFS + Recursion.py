from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def tree2str(self, node: TreeNode) -> str:
        visited = []
        self.traverse(node, visited)
        return "".join(visited)

    def traverse(self, node: TreeNode, visited: List[str]) -> None:
        if node is not None:
            visited.append(str(node.val))

            if node.left is not None or node.right is not None:
                visited.append('(')
                self.traverse(node.left, visited)
                visited.append(')')

                if node.right is not None:
                    visited.append('(')
                    self.traverse(node.right, visited)
                    visited.append(')')
