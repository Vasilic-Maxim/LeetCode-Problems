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

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        is_odd = False
        levels = []
        queue = root is not None and deque([root])
        while queue:
            # because we know how many nodes we will touch
            # we can create a list with specified length
            level = [0] * len(queue)

            for i in range(len(queue)):
                # take node
                node = queue.popleft()
                #  place it on the right spot
                level[~i if is_odd else i] = node.val

                # add children to queue
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            levels.append(level)
            is_odd ^= True
        return levels
