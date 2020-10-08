from typing import List, Any


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[Any]:
        """
        We always pay with time proportional to O(2n) because
        we iterate twice the whole list.

        Time: O(2n) => O(n)
        Space: O(k) - no auxiliary space
        """

        n = self.__length(root)
        div, mod = divmod(n, k)
        result = [None] * k
        for i in range(k):
            result[i] = root
            for _ in range(div + (mod > 0) - 1):
                root = root.next

            mod -= 1

            if root is not None:
                root.next, root = None, root.next
            else:
                break

        return result

    def __length(self, root: ListNode):
        length = 0
        while root is not None:
            length += 1
            root = root.next
        return length
