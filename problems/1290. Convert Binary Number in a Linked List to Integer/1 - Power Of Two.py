class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        decimal = 0
        while head:
            decimal = decimal * 2 + head.val
            head = head.next
        return decimal
