from collections import deque
from typing import Union


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Union[Node, None]:
        """ Time/Space: O(n) """

        if root is None:
            return root

        q = deque([root])
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()

                if i + 1 < size:
                    node.next = q[0]

                if node.left is not None:
                    q.append(node.left)
                    q.append(node.right)

        return root
