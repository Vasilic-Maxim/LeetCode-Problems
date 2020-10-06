from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    I noticed interesting thing. It is actually selection
    sort with just one exception - each time then 'slow'
    catches 'fast' a new sorted range is created. As a
    result of this algorithms we also can achieve partially
    sorted linked list. To fully sort it we can perform
    another iteration and merge ranges, which will take
    time proportional to O(n). Interesting...

    Time: O(2n) => O(n)
    Space: O(1)
    """

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        result = []
        fast_prev = None
        slow = fast = self.__reverse(head)
        while fast is not None:
            while slow.val <= fast.val and slow is not fast:
                slow = slow.next

            if slow is fast:
                result.append(0)
                fast_prev, fast = fast, fast.next
            else:
                result.append(slow.val)
                fast_prev.next, fast.next = fast.next, slow
                slow, fast = fast, fast_prev.next

        return list(reversed(result))

    def __reverse(self, node: ListNode) -> ListNode:
        new_head = None
        while node is not None:
            tmp, node.next = node.next, new_head
            new_head, node = node, tmp
        return new_head
