from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/discuss/589051/morris-algorithm-on-time-on-space
    Time: O(n)
    Space: O(n) - if we exclude tree space (because it was expected) the space complexity will be O(1)
    """
    def bstFromPreorder(self, pre_order: List[int]) -> TreeNode:
        root = current = None
        for val in pre_order:
            node = TreeNode(val)
            if current is not None:
                if node.val < current.val:
                    node.right = current
                    current.left = current = node
                else:
                    while current.right is not None and node.val > current.right.val:
                        current.right, current = None, current.right

                    node.right = current.right
                    current.right = current = node
            else:
                root = current = node

        while current.right is not None:
            current.right, current = None, current.right

        return root
