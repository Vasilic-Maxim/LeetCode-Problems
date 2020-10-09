from collections import deque
from sys import maxsize
from typing import Union


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode) -> str:
        """ Time/Space: O(n) """

        def nodes(node: TreeNode):
            if node is not None:
                yield str(node.val)
                yield from nodes(node.left)
                yield from nodes(node.right)

        return " ".join(nodes(root))

    def deserialize(self, data: str) -> Union[TreeNode, None]:
        """ Time/Space: O(n) """

        def restore(lo: int, hi: int) -> Union[TreeNode, None]:
            if items and lo < items[0] < hi:
                num = items.popleft()
                node = TreeNode(num)
                node.left = restore(lo, num)
                node.right = restore(num, hi)
                return node

        items = deque(map(int, data.split()))
        return restore(-maxsize, maxsize)
