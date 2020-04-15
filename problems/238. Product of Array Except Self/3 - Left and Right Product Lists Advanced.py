from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0] * length

        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]

        right = 1
        for i in reversed(range(length)):
            # For the index 'i', R would contain the
            # product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * right
            right *= nums[i]

        return answer
