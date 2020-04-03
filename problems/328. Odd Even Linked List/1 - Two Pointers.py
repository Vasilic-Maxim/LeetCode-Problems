class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def oddEvenList(self, head: ListNode):
        if head is None:
            return

        p1, p2, p3 = head, head.next, head.next
        while p2 is not None and p2.next:
            p1.next = p2.next
            p1 = p1.next
            p2.next = p1.next
            p2 = p2.next
            p1.next = p3

        return head
