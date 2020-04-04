class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    https://leetcode.com/problems/palindrome-linked-list/discuss/563409/Two-pointers-technique-(Python-O(n)-time-O(1)-space)
    Time: O(n)
    Space: O(1)
    """

    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        slow = fast = head
        reversed_list = None

        # reverse left half of the list while searching
        # the start point of the right half
        while fast is not None and fast.next is not None:
            tmp = slow

            # keep moving guys
            slow = slow.next
            fast = fast.next.next

            # place node at the start of the reversed half
            tmp.next = reversed_list
            reversed_list = tmp

        # if there are even number of elements in the list
        # do one more step to reach the first element of
        # the second list's half
        if fast is not None:
            slow = slow.next

        # compare reversed left half with the original
        # right half
        while reversed_list is not None and reversed_list.val == slow.val:
            reversed_list = reversed_list.next
            slow = slow.next

        return reversed_list is None
