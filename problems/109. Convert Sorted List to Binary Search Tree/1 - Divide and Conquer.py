from typing import Union


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        """
        Time: O(2n) => O(n)
        Space: O(n)
        """

        # collect all values
        values = []
        while head is not None:
            values.append(head.val)
            head = head.next

        # divide and conquer...
        def traverse(lo: int, hi: int) -> Union[TreeNode, None]:
            if lo > hi:
                return None

            mid = lo + (hi - lo) // 2
            return TreeNode(
                values[mid],
                traverse(lo, mid - 1),
                traverse(mid + 1, hi)
            )

        return traverse(0, len(values) - 1)
