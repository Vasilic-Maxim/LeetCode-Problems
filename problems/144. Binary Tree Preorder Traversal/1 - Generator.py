class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def traverse(node: TreeNode):
            if node is not None:
                yield node.val
                yield from traverse(node.left)
                yield from traverse(node.right)

        return [val for val in traverse(root)]
