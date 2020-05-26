class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, node: Node) -> int:
        if node is not None:
            return max(map(self.maxDepth, node.children), default=0) + 1
        return 0
