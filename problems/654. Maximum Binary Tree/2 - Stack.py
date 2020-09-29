from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Time: O(2n) => O(n)
    Space: O(n)
    """

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        nodes = []
        for num in nums:
            node = TreeNode(num)
            while nodes and nodes[-1].val < num:
                node.left = nodes.pop()

            if nodes:
                nodes[-1].right = node

            nodes.append(node)

        return nodes[0]
