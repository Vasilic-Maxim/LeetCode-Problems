class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    """
    Time: O(m+n)
    Space: O(1)
    """

    def getIntersectionNode(self, list_a: ListNode, list_b: ListNode):
        a = list_a
        b = list_b
        while a != b:
            a = a.next if a else list_b
            b = b.next if b else list_a
        return a
