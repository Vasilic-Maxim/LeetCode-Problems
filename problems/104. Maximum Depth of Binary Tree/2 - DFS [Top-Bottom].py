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

    def maxDepth(self, root: TreeNode) -> int:
        def traverse(node: TreeNode, depth: int) -> int:
            if node is None:
                return depth

            return max(
                traverse(node.left, depth + 1),
                traverse(node.right, depth + 1)
            )

        return traverse(root, 0)
