from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        """
        Time: O(n ** 2)
        Space: O(n)
        """

        arr = self.linked_list_to_array(head)
        self.insertion_sort(arr)
        return self.array_to_linked_list(arr)

    def linked_list_to_array(self, head: ListNode) -> List[int]:
        """ Time/Space: O(n) """

        arr = []
        while head is not None:
            arr.append(head.val)
            head = head.next

        return arr

    def insertion_sort(self, arr: List[int]) -> None:
        """
        Time: O(n ** 2)
        Space: O(1)
        """

        for i in range(1, len(arr)):
            j, tmp = i, arr[i]
            while j and tmp < arr[j - 1]:
                arr[j] = arr[j - 1]
                j -= 1

            arr[j] = tmp

    def array_to_linked_list(self, arr: List[int]) -> ListNode:
        """ Time/Space: O(n) """

        dummy = tail = ListNode()
        for val in arr:
            tail.next = tail = ListNode(val)

        return dummy.next
