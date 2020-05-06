from typing import List


class Solution:
    """
    Time: O(log n)
    Space: O(1)
    """

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters)
        while left < right:
            middle = (left + right) // 2
            if letters[middle] > target:
                right = middle
            else:
                left = middle + 1

        return letters[left] if left < len(letters) else letters[0]
