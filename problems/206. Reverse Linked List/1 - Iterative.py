class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """
    def reverseList(self, head: ListNode) -> ListNode:
        result = None
        while head:
            current = head
            head = head.next
            current.next = result
            result = current
        return result
