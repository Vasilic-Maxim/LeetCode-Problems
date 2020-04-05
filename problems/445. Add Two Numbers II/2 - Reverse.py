class ListNode:
    def __init__(self, x, next_node=None):
        self.val = x
        self.next = next_node


class Solution:
    """
    n - max(len(first), len(second))

    Time: O(n)
    Space: O(1)
    """

    def addTwoNumbers(self, first: ListNode, second: ListNode) -> ListNode:
        first_reversed = self.reverseList(first)
        second_reversed = self.reverseList(second)
        reversed_sum = self.getListsSum(first_reversed, second_reversed)
        return self.reverseList(reversed_sum)

    def reverseList(self, linked_list):
        pointer = None
        while linked_list is not None:
            tmp = linked_list.next
            linked_list.next = pointer
            pointer = linked_list
            linked_list = tmp
        return pointer

    def getListsSum(self, first: ListNode, second: ListNode) -> ListNode:
        second = ListNode(None, second)
        result = first = ListNode(None, first)
        to_add = 0
        while first.next is not None and second.next is not None:
            first, second = first.next, second.next

            to_add += first.val + second.val
            first.val = to_add % 10
            to_add //= 10

        if second.next is not None:
            first.next = second.next

        while first.next is not None:
            first = first.next

            to_add = first.val + to_add
            first.val = to_add % 10
            to_add //= 10

        if to_add:
            first.next = ListNode(to_add)

        return result.next
