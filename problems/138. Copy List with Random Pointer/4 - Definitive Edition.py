class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    """
    Time: O(3n) => O(n)
    Space: O(1)
    """

    def copyRandomList(self, head: Node):
        def nodes():
            pointer = head
            while pointer is not None:
                yield pointer
                pointer = pointer.next

        # create new nodes
        for node in nodes():
            node.random = Node(node.val, node.random, None)

        # populate random field of the new node
        for node in nodes():
            node.random.random = node.random.next and node.random.next.random

        # restore original list and build new list
        head_copy = head and head.random
        for node in nodes():
            node.random.next, node.random = node.next and node.next.random, node.random.next

        return head_copy
