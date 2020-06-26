from collections import deque
from typing import Tuple, Deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    BFS is not the most efficient way to solve that problem
    because of the space complexity.

    Time: O(n)
    Space (any tree): O(n)
    """

    def sumNumbers(self, root: TreeNode) -> int:
        queue: Deque[Tuple[TreeNode, int]] = deque([(root, 0)])
        result = 0
        while queue:
            node, path = queue.popleft()

            if node is not None:
                path = path * 10 + node.val

                if node.left is None and node.right is None:
                    result += path
                else:
                    queue.append((node.left, path))
                    queue.append((node.right, path))

        return result
