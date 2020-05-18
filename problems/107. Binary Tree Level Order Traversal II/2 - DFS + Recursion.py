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

    def __init__(self):
        self.levels: List[List[int]] = []

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        self.dfs(root, 0)
        self.levels.reverse()
        return self.levels

    def dfs(self, node: TreeNode, level: int):
        if node is not None:
            if level == len(self.levels):
                self.levels.append([])

            self.levels[level].append(node.val)
            self.dfs(node.left, level + 1)
            self.dfs(node.right, level + 1)
