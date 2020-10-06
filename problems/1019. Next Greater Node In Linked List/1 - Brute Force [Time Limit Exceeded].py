from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Time: O(n ** 2)
    Space: O(n)
    """

    def nextLargerNodes(self, node: ListNode) -> List[int]:
        result = []
        while node is not None:
            next_largest = node.next
            while next_largest is not None and next_largest.val <= node.val:
                next_largest = next_largest.next

            result.append(0 if next_largest is None else next_largest.val)
            node = node.next

        return result
