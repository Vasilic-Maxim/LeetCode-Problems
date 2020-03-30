class Solution:
    """
    Time: O(log_n) - logarithmic because we divide by 2 repeatedly
    Space: O(1)
    """
    def numberOfSteps(self, num: int) -> int:
        counter = 0
        while num:
            num = num // 2 if num % 2 == 0 else num - 1
            counter += 1
        return counter
