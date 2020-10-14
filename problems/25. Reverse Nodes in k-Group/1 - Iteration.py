class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        n = self.count(head)
        dummy = p1 = ListNode(0, head)
        for _ in range(n // k):
            p2 = p1.next
            for _ in range(k - 1):
                tmp = p2.next
                p2.next = tmp.next
                tmp.next = p1.next
                p1.next = tmp
            p1 = p2
        return dummy.next

    def count(self, head: ListNode) -> int:
        count = 0
        while head is not None:
            count += 1
            head = head.next
        return count
