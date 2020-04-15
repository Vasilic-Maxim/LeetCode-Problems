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
    def convertBST(self, node: TreeNode) -> TreeNode:
        root, total = node, 0
        stack = []
        while stack or node is not None:
            while node is not None:
                stack.append(node)
                node = node.right

            node = stack.pop()
            total += node.val
            node.val = total
            node = node.left
        return root
