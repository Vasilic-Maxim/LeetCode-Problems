from collections import defaultdict
from typing import DefaultDict, Any


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def copyRandomList(self, head: Node):
        # store relations between old and new nodes
        memo: DefaultDict[Any, Any] = defaultdict(lambda: Node(-1))
        memo[None] = None

        # create nodes without random links
        pointer = head
        while pointer is not None:
            memo[pointer].val = pointer.val
            memo[pointer].next = memo[pointer.next]
            memo[pointer].random = memo[pointer.random]
            pointer = pointer.next

        return memo[head]
