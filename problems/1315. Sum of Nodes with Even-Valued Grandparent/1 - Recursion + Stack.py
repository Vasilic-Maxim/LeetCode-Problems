from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        """
        h = tree height
        Time: O(n)
        Space: O(2 * height) => O(height)
        """

        return self.traverse(root, [])

    def traverse(self, node: TreeNode, path: List[int]) -> int:
        nodes_sum = 0
        if node is not None:
            n = len(path)
            if n >= 2 and path[n - 2] % 2 == 0:
                nodes_sum += node.val

            path.append(node.val)
            nodes_sum += self.traverse(node.left, path)
            nodes_sum += self.traverse(node.right, path)
            path.pop()
        return nodes_sum
