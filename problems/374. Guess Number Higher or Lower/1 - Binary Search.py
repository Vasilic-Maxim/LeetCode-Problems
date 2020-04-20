# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    """
    Time: O(log n)
    Space: O(1)
    """
    def guessNumber(self, right: int) -> int:
        left = 0
        while left <= right:
            middle = (left + right) // 2
            correctness = guess(middle)
            if not correctness:
                return middle

            if correctness == 1:
                left = middle + 1
            else:
                right = middle - 1
