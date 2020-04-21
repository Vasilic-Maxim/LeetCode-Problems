from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """
    def preorder(self, root: Node) -> List[int]:
        result = []

        if root is not None:
            self.traverse(root, result)

        return result

    def traverse(self, node: Node, result: list):
        result.append(node.val)

        for child in node.children:
            self.traverse(child, result)
