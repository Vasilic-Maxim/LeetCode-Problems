class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    """
    Time: O(2n) => O(n)
    Space: O(n)
    """

    def copyRandomList(self, head: Node):
        # store relations between old and new nodes
        memo = {}

        # create nodes without random links
        p1 = p2 = head
        while p1 is not None:
            memo[p1] = Node(p1.val)
            p1 = p1.next

        # add random links to all new nodes
        while p2 is not None:
            memo[p2].next = memo.get(p2.next)
            memo[p2].random = memo.get(p2.random)
            p2 = p2.next

        return memo.get(head)
