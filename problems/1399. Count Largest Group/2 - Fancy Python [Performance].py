from statistics import multimode


class Solution:
    """
    Approximately 40% boost with use of 'digit_sum' method
    """

    def countLargestGroup(self, n: int) -> int:
        return len(multimode(map(self.digit_sum, range(1, n + 1))))

    def digit_sum(self, num: int) -> int:
        """
        Time: O(log (n))
        Space: O(1)
        """
        result = 0
        while num:
            num, digit = divmod(num, 10)
            result += digit
        return result
