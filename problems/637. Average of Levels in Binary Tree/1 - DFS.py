from collections import deque
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

    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = deque([root])
        result = []
        while queue:
            length = len(queue)
            level_sum = 0
            for _ in range(length):
                node = queue.popleft()
                level_sum += node.val

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result.append(level_sum / length)
        return result
