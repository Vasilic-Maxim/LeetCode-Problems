from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        result = ListNode()
        for item in lists:
            result = self.merge(result, item)
        return result.next

    def merge(self, first: ListNode, second: ListNode) -> ListNode:
        head = first
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

        return head
