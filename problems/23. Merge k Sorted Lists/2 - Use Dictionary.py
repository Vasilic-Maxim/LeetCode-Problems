from collections import defaultdict
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # create dictionary of nodes and values
        nodes = defaultdict()
        for item in lists:
            while item is not None:
                tmp = item.next
                item.next = nodes[item.val]
                nodes[item.val] = item
                item = tmp

        # connect the nodes
        result = pointer = ListNode()
        for key in sorted(nodes.keys()):
            pointer.next = nodes[key]
            while pointer.next is not None:
                pointer = pointer.next

        pointer.next = None

        return result.next
