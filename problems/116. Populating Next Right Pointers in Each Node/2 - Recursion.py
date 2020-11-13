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
        Space: O(log (n))
        """

        def traverse(left: Node, right: Node):
            if left is None or left.next is right:
                return

            left.next = right
            traverse(left.left, left.right)
            traverse(left.right, right.left)
            traverse(right.left, right.right)

        if root is not None:
            traverse(root.left, root.right)

        return root

