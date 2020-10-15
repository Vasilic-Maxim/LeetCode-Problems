from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        """
        Time: O(n)
        Space: O(height)
        """

        path = [root]
        nodes_sum = 0
        while path:
            node = path[-1]
            if node.left is not None:
                path.append(node.left)
                node.left = None
            elif node.right is not None:
                path.append(node.right)
                node.right = None
            else:
                n = len(path)
                if n >= 3 and path[n - 3].val % 2 == 0:
                    nodes_sum += node.val
                path.pop()
        return nodes_sum
