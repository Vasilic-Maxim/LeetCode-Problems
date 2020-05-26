from typing import List


class Solution:
    """
    Example: [-4, -1, 0, 3, 10]
    Representation of all absolute numbers from the list
             /
    \      /
     \   /
      \/

    Int that case compare values from the start and end of the
    list and always insert the biggest one because we do not know
    the lowest position in the list.

    Time: O(n)
    Space: O(n)
    """

    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        left, right = 0, len(nums) - 1
        while left <= right:
            left, right = abs(nums[left]), abs(nums[right])
            if left > right:
                answer[right - left] = left * left
                left += 1
            else:
                answer[right - left] = right * right
                right -= 1
        return answer
