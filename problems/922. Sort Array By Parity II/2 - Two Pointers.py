from typing import List


class Solution:
    """
    Slow pointer goes only thorough even numbers
    Fast, only through odd numbers

    Time: O(n)
    Space: O(1)
    """

    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        fast = 1
        for slow in range(0, len(nums), 2):
            if nums[slow] % 2:
                while nums[fast] % 2:
                    fast += 2
                nums[slow], nums[fast] = nums[fast], nums[slow]
        return nums
