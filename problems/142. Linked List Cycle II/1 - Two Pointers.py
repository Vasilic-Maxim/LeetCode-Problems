class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """
    def detectCycle(self, head: ListNode):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                break
        else:
            return

        while head is not slow:
            slow = slow.next
            head = head.next

        return head
