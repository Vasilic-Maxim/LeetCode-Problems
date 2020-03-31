from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    n - number of elements in tree
    Time: O(n)
    Space: O(n) - set (if all elements are unique and no sum that matches the target)
    """
    def findTarget(self, root: TreeNode, target: int) -> bool:
        if root is None:
            return False

        wanted = set()
        queue = deque()
        queue.append(root)
        while len(queue):
            node = queue.popleft()
            if node is None:
                continue

            if node.val in wanted:
                return True

            wanted.add(target - node.val)
            queue.append(node.left)
            queue.append(node.right)

        return False
