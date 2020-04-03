class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):
        current = pointer = head

        if n == 1 and head.next is None:
            return

        for _ in range(n):
            current = current.next

        if current is None:
            return head.next

        while True:
            if current.next is None:
                pointer.next = pointer.next.next
                return head

            current = current.next
            pointer = pointer.next
