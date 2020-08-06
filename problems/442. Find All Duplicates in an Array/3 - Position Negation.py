from typing import List


class Solution:
    """
    Thoughts:
    ------------------------------------------------------------------
    Truth:      We know that there are n positive numbers from [1-n]
    Conclusion: Each number (num) from that range can take position
                equivalent to (num - 1). For example:

                Initial range:      [1,2,3,4,5,6,7,8]
                With duplicates:    [1,2,2,4,5,6,6,8]

                NOTE: The real input might not be sorted!
    ------------------------------------------------------------------
    Truth:      If there are any duplicates in the input list then
                the duplicate number will indicate on the same index
                as the original one.
    Conclusion: We can modify the value on index that can be calculated
                with the formula (num - 1). The best way to modify the
                value on specific index is by negating it. Negation is
                best choice because negative number can easily become
                positive with help of abs() function.
    ------------------------------------------------------------------
    Truth:      When you first time met the the number that is
                duplicated you negate the value on index (num - 1).
    Conclusion: If current number points on index with negative value
                then we found a duplicate!
    ------------------------------------------------------------------
    Time: O(n)
    Space: O(1)
    """

    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                result.append(abs(num))
            else:
                nums[index] *= -1
        return result
