from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def isOneBitCharacter(self, bits: List[int]) -> bool:
        pointer = 0
        while pointer < len(bits) - 1:
            pointer += bits[pointer] + 1
        return pointer == len(bits) - 1
