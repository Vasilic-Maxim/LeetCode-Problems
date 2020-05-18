from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        stack = [(root, 0)]
        levels = []

        while stack:
            node, level = stack.pop()
            if node is not None:
                if level == len(levels):
                    levels.append([])
                levels[level].append(node.val)
                stack.append((node.right, level + 1))
                stack.append((node.left, level + 1))
        levels.reverse()
        return levels
