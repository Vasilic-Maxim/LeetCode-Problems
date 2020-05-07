class ListNode:
    def __init__(self, x: int, next_node=None):
        self.val = x
        self.next = next_node


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def swapPairs(self, head: ListNode) -> ListNode:
        current = result = ListNode(-1, head)
        while current.next is not None and current.next.next is not None:
            first, second = current.next, current.next.next
            first.next = second.next
            current.next = current = second
            current.next = current = first

        return result.next
