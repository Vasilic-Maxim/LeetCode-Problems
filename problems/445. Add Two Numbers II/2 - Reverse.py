class ListNode:
    def __init__(self, x, next_node=None):
        self.val = x
        self.next = next_node


class Solution:
    """
    n - max(len(first), len(second))

    Time: O(n)
    Space: O(1)
    """

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        reversed1 = self.reverse(l1)
        reversed2 = self.reverse(l2)
        result = self.merge(reversed1, reversed2)
        return self.reverse(result)

    def reverse(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        while head is not None:
            tmp = head.next
            head.next = dummy.next
            dummy.next = head
            head = tmp

        return dummy.next

    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = l1 = ListNode(0, l1)
        carry = 0
        while l1.next is not None and l2 is not None:
            carry, l1.next.val = divmod(l1.next.val + l2.val + carry, 10)
            l1, l2 = l1.next, l2.next

        if l2 is not None:
            l1.next = l2

        while l1.next is not None and carry:
            l1 = l1.next
            carry, l1.val = divmod(l1.val + carry, 10)

        if carry:
            l1.next = ListNode(carry)

        return dummy.next
