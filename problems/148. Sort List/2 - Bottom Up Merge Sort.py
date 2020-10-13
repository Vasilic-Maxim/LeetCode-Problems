from typing import Union, Tuple, Any


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Time: O(n * log (n))
    Space: O(1)
    """

    def sortList(self, head: ListNode) -> Union[ListNode, None]:
        if head is None or head.next is None:
            return head

        size = self.get_size(head)
        dummy = ListNode(-1, head)
        step = 1
        while step < size:
            pointer = dummy
            for _ in range(size // step):
                first = pointer.next
                second = self.divide(first, step)
                reminder = self.divide(second, step)
                pointer.next, pointer = self.merge(first, second)
                pointer.next = reminder
            step *= 2

        return dummy.next

    def get_size(self, head: ListNode) -> int:
        size = 0
        while head is not None:
            head = head.next
            size += 1
        return size

    def divide(self, head: ListNode, size: int) -> Union[ListNode, None]:
        if head is None:
            return head

        for _ in range(1, size):
            if head.next is None:
                return None
            head = head.next

        tail = head.next
        head.next = None
        return tail

    def merge(self, first: ListNode, second: ListNode) -> Tuple[Any, Union[ListNode, Any]]:
        dummy = first = ListNode(0, first)
        while first.next is not None and second is not None:
            if first.next.val < second.val:
                first = first.next
            else:
                tmp = first.next
                first.next = second
                first, second = second, second.next
                first.next = tmp

        if second is not None:
            first.next = second

        while first.next is not None:
            first = first.next

        return dummy.next, first
