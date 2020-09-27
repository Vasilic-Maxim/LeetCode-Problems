from typing import List


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

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def traverse(node: TreeNode):
            if node is not None:
                yield from traverse(node.left)
                yield from traverse(node.right)
                yield node.val

        return [val for val in traverse(root)]
