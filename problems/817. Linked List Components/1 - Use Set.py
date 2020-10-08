from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Time: O(n + m)
    Space: O(m)
    """

    def numComponents(self, head: ListNode, nums: List[int]) -> int:
        subset = set(nums)
        counter = 0
        while head is not None:
            if head.val in subset and getattr(head.next, "val", None) not in subset:
                counter += 1
            head = head.next
        return counter