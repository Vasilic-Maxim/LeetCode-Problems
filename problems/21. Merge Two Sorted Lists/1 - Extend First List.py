class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """
    def mergeTwoLists(self, first: ListNode, second: ListNode):
        pointer = first = ListNode(None, first)
        while pointer.next is not None and second is not None:
            if pointer.next.val > second.val:
                tmp = pointer.next
                pointer.next = second
                second = second.next
                pointer.next.next = tmp

            pointer = pointer.next

        if second is not None:
            pointer.next = second

        return first.next
