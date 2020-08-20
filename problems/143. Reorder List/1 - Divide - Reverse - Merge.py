class ListNode:
    def __init__(self, val=0, following=None):
        self.val = val
        self.next = following


class Solution:
    def reorderList(self, initial: ListNode) -> None:
        # Empty list
        if initial is None:
            return

        middle = self.half(initial)

        # if there si just one node
        if middle is initial:
            return

        # if there are only 2 nodes
        # if middle is initial.next:
        #     return

        # cut the list into two pieces
        second_half = self.reverse(middle)
        self.merge(initial, second_half)

    def half(self, head: ListNode) -> ListNode:
        slow = fast = head
        prev = None
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if slow is fast:
            return slow

        if fast is not None:
            prev = prev.next
            slow = slow.next

        prev.next = None

        return slow

    def reverse(self, head: ListNode) -> ListNode:
        pointer = head.next
        head.next = None
        while pointer is not None:
            tmp = pointer.next
            pointer.next = head
            head, pointer = pointer, tmp
        return head

    def merge(self, first: ListNode, second: ListNode) -> None:
        while second is not None:
            tmp = first.next
            first.next = first = second
            second = second.next
            first.next = first = tmp
