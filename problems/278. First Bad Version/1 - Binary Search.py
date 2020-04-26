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
        min_bad = n
        p1 = 1
        p2 = n
        while p1 != p2:
            center = p1 + (p2 - p1) // 2
            if isBadVersion(center):
                p2 = min_bad = center
            else:
                p1 = center + 1

        return min_bad