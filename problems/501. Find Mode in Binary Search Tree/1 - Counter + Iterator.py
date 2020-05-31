from collections import Counter
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if root is not None:
            most_common = Counter(self.dfs(root)).most_common()
            max_val = most_common[0][1]
            return [key for key, val in most_common if val == max_val]
        return []

    def dfs(self, node):
        if node is not None:
            yield node.val
            yield from self.dfs(node.left)
            yield from self.dfs(node.right)
