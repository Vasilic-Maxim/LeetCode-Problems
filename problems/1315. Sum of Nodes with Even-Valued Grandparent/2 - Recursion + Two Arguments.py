class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        """
        Time: O(n)
        Space: O(height)
        """

        return self.traverse(root, 1, 1)

    def traverse(self, node: TreeNode, parent: int, grandparent: int) -> int:
        nodes_sum = 0
        if node is not None:
            if grandparent % 2 == 0:
                nodes_sum += node.val

            nodes_sum += self.traverse(node.left, node.val, parent)
            nodes_sum += self.traverse(node.right, node.val, parent)
        return nodes_sum
