from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """
    def duplicateZeros(self, nums: List[int]) -> None:
        possible_zeros = 0
        length = len(nums) - 1

        for left in range(length + 1):
            if left > length - possible_zeros:
                break

            if not nums[left]:
                # Edge case: This zero can't be duplicated. We have no more space,
                # as left is pointing to the last element which could be included
                if left == length - possible_zeros:
                    nums[length] = 0  # For this zero we just copy it without duplication.
                    length -= 1
                    break
                possible_zeros += 1

        # Start backwards from the last element which would be part of new list.
        last = length - possible_zeros

        for i in range(last, -1, -1):
            nums[i + possible_zeros] = nums[i]

            if not nums[i]:
                possible_zeros -= 1
                nums[i + possible_zeros] = 0
