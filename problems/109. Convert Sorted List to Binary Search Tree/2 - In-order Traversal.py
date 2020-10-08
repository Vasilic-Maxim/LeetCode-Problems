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
    def sortedListToBST(self, head: ListNode) -> Union[TreeNode, None]:
        size = 0
        pointer = head
        while pointer is not None:
            size += 1
            pointer = pointer.next

        def convert(lo: int, hi: int) -> Union[TreeNode, None]:
            nonlocal head

            if lo > hi:
                return None

            mid = (lo + hi) // 2
            left = convert(1, mid - 1)
            node = TreeNode(head.val)
            head = head.next
            node.left, node.right = left, convert(mid + 1, hi)
            return node

        return convert(0, size - 1)
