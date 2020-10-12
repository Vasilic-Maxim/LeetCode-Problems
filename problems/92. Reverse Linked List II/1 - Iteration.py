class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = pointer = ListNode(-1, head)
        for _ in range(m - 1):
            pointer = pointer.next

        pointer.next = self.reverse(pointer.next, n - m)
        return dummy.next

    def reverse(self, head: ListNode, steps: int) -> ListNode:
        p1, p2 = head, head.next
        for _ in range(steps):
            p1.next, p2.next = p2.next, head
            head, p2 = p2, p1.next

        return head
