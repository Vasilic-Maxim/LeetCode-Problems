class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def maxDepth(self, root: TreeNode) -> int:
        stack = root is not None and [(root, 1)]
        max_depth = 0
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)

            if node.right is not None:
                stack.append((node.right, depth + 1))
            if node.left is not None:
                stack.append((node.left, depth + 1))

        return max_depth
