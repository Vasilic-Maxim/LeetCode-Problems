class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    """
    m - len(list_a)
    n - len(list_b)
    Time : O(m+n)
    Space: O(m)
    """

    def getIntersectionNode(self, list_a: ListNode, list_b: ListNode):
        data = set()
        while list_a:
            data.add(list_a)
            list_a = list_a.next
        while list_b:
            if list_b in data:
                return list_b
            list_b = list_b.next
        return
