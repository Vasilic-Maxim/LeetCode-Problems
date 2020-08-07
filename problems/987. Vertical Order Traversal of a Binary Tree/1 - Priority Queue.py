import heapq
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
    Space: O(n * log(n))
    """

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        level_items = deque([(root, 0)])
        level = offset = 0
        coordinates = []
        while level_items:
            for _ in range(len(level_items)):
                node, position = level_items.pop()
                offset = min(offset, position)

                # add coordinate
                coordinates.append((level, position, node.val))

                # create next level
                if node.left is not None:
                    level_items.appendleft((node.left, position - 1))
                if node.right is not None:
                    level_items.appendleft((node.right, position + 1))

            # move to the next level
            level += 1

        heapq.heapify(coordinates)
        traversal: List[List[int]] = [[] for _ in range(abs(offset))]
        while coordinates:
            _, x, value = heapq.heappop(coordinates)

            if x < len(traversal) + offset:
                traversal[x - offset].append(value)
            else:
                traversal.append([value])

        return traversal
