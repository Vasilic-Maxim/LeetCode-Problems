class ListNode:
    def __init__(self, x, next_node=None):
        self.val = x
        self.next = next_node


class Solution:
    """
    https://leetcode.com/problems/add-two-numbers/discuss/564902/extend-first-list-python-on-time-o1-space
    n - max(len(first), len(second))
    Time: O(n)
    Space: O(1)
    """

    def addTwoNumbers(self, first: ListNode, second: ListNode) -> ListNode:
        second = ListNode(None, second)
        result = first = ListNode(None, first)
        to_add = 0

        # go throughout the common number of nodes and compute
        # their sum
        while first.next is not None and second.next is not None:
            first, second = first.next, second.next
            # lines below can be replaced with (read note):
            # to_add, first.val = divmod(first.val + second.val + to_add, 10)
            to_add += first.val + second.val
            first.val = to_add % 10
            to_add //= 10

        # if there are any elements left in the second list
        # then add them to the first list
        if second.next is not None:
            first.next = second.next

        # compute sums to remaining elements
        while first.next is not None:
            first = first.next
            # lines below can be replaced with (read note):
            # to_add, first.val = divmod(first.val + to_add, 10)
            to_add = first.val + to_add
            first.val = to_add % 10
            to_add //= 10

        # create a new node for remainder if it is not empty
        if to_add:
            first.next = ListNode(to_add)

        return result.next
