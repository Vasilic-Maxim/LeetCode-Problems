class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current and current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next
