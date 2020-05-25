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

    def rangeSumBST(self, root: TreeNode, left: int, right: int) -> int:
        stack = [root]
        result = 0
        while stack:
            node = stack.pop()
            if node is not None:
                if left <= node.val <= right:
                    result += node.val

                if right > node.val:
                    stack.append(node.right)
                if left < node.val:
                    stack.append(node.left)
        return result
