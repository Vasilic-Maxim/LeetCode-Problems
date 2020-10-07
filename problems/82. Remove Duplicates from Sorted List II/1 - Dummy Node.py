class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def deleteDuplicates(self, head: ListNode) -> [None, ListNode]:
        if head is None:
            return None

        dummy = p1 = ListNode(-1, head)
        while p1.next is not None:
            p2 = p1.next
            counter, wanted = 0, p2.val
            while p2 is not None and p2.val == wanted:
                counter += 1
                p2 = p2.next

            if counter > 1:
                p1.next = p2
            else:
                p1 = p1.next

        return dummy.next
