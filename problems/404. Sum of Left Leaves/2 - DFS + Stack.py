class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    ===== Unbalanced BST =====
    Time: O(n)
    Space: O(n)

    ===== Balanced BST =====
    Time: O(n)
    Space: O(log (n))
    """

    def sumOfLeftLeaves(self, node: TreeNode) -> int:
        stack = [(node, False)]
        left_sum = 0
        while stack:
            node, is_left = stack.pop()
            if node is not None:
                if node.left is None and node.right is None and is_left:
                    left_sum += node.val
                else:
                    stack.append((node.right, False))
                    stack.append((node.left, True))
        return left_sum
