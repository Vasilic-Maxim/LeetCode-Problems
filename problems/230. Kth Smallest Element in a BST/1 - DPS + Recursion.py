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

    def kthSmallest(self, node: TreeNode, k: int) -> int:
        self.in_order_traversal(node, (result := []))
        return result[k - 1]

    def in_order_traversal(self, node: TreeNode, order: List[int]):
        if node:
            self.in_order_traversal(node.left, order)
            order.append(node.val)
            self.in_order_traversal(node.right, order)
