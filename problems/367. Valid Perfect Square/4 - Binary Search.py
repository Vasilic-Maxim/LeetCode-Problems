class Solution:
    """
    Time: O(log n)
    Space: O(1)
    """

    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        while left <= right:
            mid = (left + right) // 2
            square = mid ** 2
            if square == num:
                return True
            elif square > num:
                right = mid - 1
            else:
                left = mid + 1
        return False
