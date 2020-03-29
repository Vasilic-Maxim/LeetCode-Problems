from collections import Counter

"""
n - len(nums1)
m - len(nums2)
Time: O(n + m)
Space: O(min(n, m))
"""


class Solution:
    def intersect(self, nums1: list, nums2: list) -> list:
        return (Counter(nums1) & Counter(nums2)).elements()
