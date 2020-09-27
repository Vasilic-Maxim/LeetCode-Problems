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
    Space: O(2n) => O(n)
    """

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = root is not None and deque([root])
        result = []
        while queue:
            result.append([])

            for _ in range(len(queue)):
                node = queue.popleft()
                result[-1].append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return result
