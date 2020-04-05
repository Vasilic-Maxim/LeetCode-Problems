class ListNode:
    def __init__(self, x, next_node=None):
        self.val = x
        self.next = next_node


class Solution:
    """
    n - max(len(first), len(second))

    Time: O(n)
    Space: O(n)
    """
    def addTwoNumbers(self, first: ListNode, second: ListNode) -> ListNode:
        nums_sum = self.getNumber(first) + self.getNumber(second)
        result = None

        # make at least one iteration, special for zero-lists
        while nums_sum or result is None:
            result = ListNode(nums_sum % 10, result)
            nums_sum //= 10

        return result

    def getNumber(self, nums_list: ListNode) -> int:
        num = 0
        while nums_list is not None:
            num = num * 10 + nums_list.val
            nums_list = nums_list.next
        return num
