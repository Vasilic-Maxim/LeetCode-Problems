from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, node: Node) -> List[int]:
        stack = node is not None and [node]
        result = []

        while stack:
            for _ in range(len(stack)):
                node = stack[-1]
                if node.children:
                    stack.extend(reversed(node.children))
                    node.children = None
                else:
                    result.append(stack.pop().val)

        return result
