class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int):
        if head is None:
            return None

        # find out the length
        tail, length = head, 1
        while tail.next is not None:
            tail = tail.next
            length += 1

        # no need to modify
        if length == k:
            return head

        # connect tail with head and do steps necessary
        tail.next = head
        for _ in range(length - k % length):
            tail = tail.next

        # split the list
        head = tail.next
        tail.next = None

        return head
