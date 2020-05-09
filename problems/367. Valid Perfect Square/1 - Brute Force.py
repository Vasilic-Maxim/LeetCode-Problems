class Solution:
    """
    Time: O(sqrt(num))
    Space: O(1)
    """

    def isPerfectSquare(self, num: int) -> bool:
        guess = 1
        while guess * guess < num:
            guess += 1
        return guess * guess == num
