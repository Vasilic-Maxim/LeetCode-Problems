from collections import deque
from typing import Deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Time: O(n ** 2)
    Space: O(n)
    """

    def insertionSortList(self, head: ListNode) -> ListNode:
        q: Deque[ListNode] = deque()
        while head is not None:
            item, head = head, head.next
            item.next = None
            i = len(q) - 1
            while i >= 0 and q[i].val > item.val:
                i -= 1

            if i >= 0:
                q[i].next = item
            if i + 1 < len(q):
                item.next = q[i + 1]
            q.insert(i + 1, item)

        return q[0] if q else None
