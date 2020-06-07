from math import sqrt


class Solution:
    """
    Time: O(sqrt(n))
    Space: O(1)
    """

    # The same result you will get from the code below.
    # The code below is more elegant, however it is
    # slower.
    #
    # def judgeSquareSum(self, c: int) -> bool:
    #     for a in range(int(sqrt(c)) + 1):
    #         b = sqrt(c - a * a)
    #         if b == int(b):
    #             return True
    #     return False

    def judgeSquareSum(self, n: int) -> bool:
        return any(self.is_perfect_square(n - a * a) for a in range(int(sqrt(n)) + 1))

    def is_perfect_square(self, s):
        return int(sqrt(s)) ** 2 == s
