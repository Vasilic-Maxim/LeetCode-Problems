class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


class Solution(object):
    def mergeTwoLists(self, first, second):
        result = current = ListNode(0)
        while first and second:
            if first.val < second.val:
                current.next = first
                first = first.next
            else:
                current.next = second
                second = second.next
            current = current.next

        if first is not None:
            current.next = first
        elif second is not None:
            current.next = second

        return result.next
