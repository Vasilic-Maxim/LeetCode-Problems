# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    """
    Time: O(log n)
    Space: O(1)
    """

    def firstBadVersion(self, n):
        left = 1
        right = n
        while left < right:
            center = (left + right) // 2
            if isBadVersion(center):
                right = center
            else:
                left = center + 1

        return right
