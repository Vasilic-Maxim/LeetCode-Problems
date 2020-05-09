class Solution:
    """
    Time: O(log n)
    Space: O(1)
    """
    def isPerfectSquare(self, num: int) -> bool:
        guess = num
        while guess * guess > num:
            guess = (guess + num / guess) // 2
        return guess * guess == num
