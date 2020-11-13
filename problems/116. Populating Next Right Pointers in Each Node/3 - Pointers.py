from typing import Union


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Union[Node, None]:
        """
        Time: O(n)
        Space: O(1)
        """

        if root is None:
            return root

        head = tail = root
        while tail.left is not None:
            tail.left.next = tail.right
            if tail.next is not None:
                tail.right.next = tail.next.left
                tail = tail.next
            else:
                head = tail = head.left

        return root
