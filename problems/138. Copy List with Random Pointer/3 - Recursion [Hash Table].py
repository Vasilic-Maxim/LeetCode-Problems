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
        return self.copy(head, {})

    def copy(self, head: Node, memo: dict):
        if head is None:
            return None

        memo[head] = Node(head.val)
        memo[head].next = self.copy(head.next, memo)
        memo[head].random = memo.get(head.random)

        return memo[head]
