class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def flatten(self, root: TreeNode) -> None:
        if root is None:
            return

        def nodes(node: TreeNode) -> tuple:
            if node is not None:
                left, right = node.left, node.right
                node.left = node.right = None
                yield node
                yield from nodes(left)
                yield from nodes(right)

        it = iter(nodes(root))
        parent = next(it)
        for node in it:
            parent.right = parent = node
