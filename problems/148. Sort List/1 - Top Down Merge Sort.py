from typing import Union


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Time: O(n * log (n))
    Space: O(log (n))
    """

    def sortList(self, first: ListNode) -> Union[ListNode, None]:
        if first is None or first.next is None:
            return first

        second = self.divide(first)
        first = self.sortList(first)
        second = self.sortList(second)
        return self.merge(first, second)

    def divide(self, head: ListNode) -> ListNode:
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return mid

    def merge(self, first: ListNode, second: ListNode) -> ListNode:
        dummy = first = ListNode(0, first)
        while first.next is not None and second is not None:
            if first.next.val < second.val:
                first = first.next
            else:
                tmp = first.next
                first.next = second
                first, second = first.next, second.next
                first.next = tmp

        if second is not None:
            first.next = second

        return dummy.next
