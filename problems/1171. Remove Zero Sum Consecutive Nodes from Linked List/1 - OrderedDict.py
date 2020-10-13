from collections import OrderedDict
from typing import Union


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Time/Space: O(n)
    """

    def removeZeroSumSublists(self, head: ListNode) -> Union[ListNode, None]:
        cur = dummy = ListNode(0, head)
        seen = OrderedDict()
        prefix = 0
        while cur:
            prefix += cur.val
            node = seen.get(prefix, cur)
            while prefix in seen:
                seen.popitem()
            seen[prefix] = node
            node.next = cur = cur.next
        return dummy.next
