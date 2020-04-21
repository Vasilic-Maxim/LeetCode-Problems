from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val: int = val
        self.children: list = children


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def preorder(self, root: Node) -> List[int]:
        result, stack = [], root is not None and [root]

        while stack:
            node = stack.pop()
            result.append(node.val)
            # alternative, but less time efficient
            # stack.extend(reversed(node.children))
            for child in reversed(node.children):
                stack.append(child)

        return result
