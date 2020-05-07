from collections import deque


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

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = deque([root])
        while len(queue):
            cache = {}
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left is not None:
                    cache[node.left.val] = node.val
                    queue.append(node.left)
                if node.right is not None:
                    cache[node.right.val] = node.val
                    queue.append(node.right)

            if x in cache and y in cache and cache[x] != cache[y]:
                return True
            if x in cache or y in cache:
                return False
