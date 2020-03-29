"""
All Solutions have same complexities
Time: O(n)
Space: O(1)
"""


class Solution:
    def reverseString(self, s: list) -> None:
        s[:] = s[::-1]
