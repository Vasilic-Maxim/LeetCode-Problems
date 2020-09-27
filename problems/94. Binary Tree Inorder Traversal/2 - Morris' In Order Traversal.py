from typing import List


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

    def inorderTraversal(self, node: TreeNode) -> List[int]:
        result = []

        while node is not None:
            if node.left is None:
                result.append(node.val)
                node = node.right
            else:
                tmp = node
                node = sibling = node.left
                while sibling and sibling.right:
                    sibling = sibling.right
                sibling.right = tmp
                tmp.left = None

        return result
