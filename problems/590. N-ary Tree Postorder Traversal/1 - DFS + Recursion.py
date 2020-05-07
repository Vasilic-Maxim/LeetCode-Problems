from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, node: Node, res=None) -> List[int]:
        if res is None:
            res = []
        if node is not None:
            if node.children is not None:
                for child in node.children:
                    self.postorder(child, res)
            res.append(node.val)

        return res
