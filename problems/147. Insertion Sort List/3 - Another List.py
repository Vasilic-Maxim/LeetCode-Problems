class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Time: O(n ** 2)
    Space: O(1)
    """

    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = tail = ListNode()
        while head is not None:
            tmp = head.next
            tail = self.insert(dummy, tail, head)
            head = tmp

        return dummy.next

    def insert(self, dummy: ListNode, tail: ListNode, node: ListNode) -> ListNode:
        if tail is not dummy and node.val > tail.val:
            tail.next = tail = node
            tail.next = None
        else:
            pointer = dummy
            while pointer.next is not None and pointer.next.val < node.val:
                pointer = pointer.next

            node.next, pointer.next = pointer.next, node

        return tail
