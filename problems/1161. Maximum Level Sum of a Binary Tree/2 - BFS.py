from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        """ Time/Space: O(n) """

        q = deque([root])
        max_sum = float("-inf")
        max_sum_level = None
        level = 1
        while q:
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val

                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)

            if level_sum > max_sum:
                max_sum, max_sum_level = level_sum, level

            level += 1

        return max_sum_level
