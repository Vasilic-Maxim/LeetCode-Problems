class ListNode:
    def __init__(self, x, next_node=None):
        self.val = x
        self.next = next_node


class Solution:
    """
    n - number of digits in the result

    Time: O(n)
    Space: O(n)
    """
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = n2 = 0
        while l1 is not None:
            n1 = n1 * 10 + l1.val
            l1 = l1.next

        while l2 is not None:
            n2 = n2 * 10 + l2.val
            l2 = l2.next

        carry = n1 + n2
        result = None
        while carry or result is None:
            carry, val = divmod(carry, 10)
            result = ListNode(val, result)

        return result
