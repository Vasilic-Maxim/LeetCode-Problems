from typing import List, Any


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[Any]:
        """
        We always pay with time proportional to O(n + k). The worst
        case arises when k > n.

        Time: O(n + k)
        Space: O(n + k)
        """

        ids = []
        while root is not None:
            ids.append(root)
            root = root.next

        result = [None] * k
        div, mod = divmod(len(ids), k)
        start = 0
        for i in range(k):
            if start < len(ids):
                result[i] = ids[start]
                start += div + (mod > 0)
                ids[start - 1].next = None
                mod -= 1

        return result
