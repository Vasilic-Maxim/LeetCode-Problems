"""
n - len(max_list)
m - len(min_list)
Time: O(m^2)
Space: O(m)
"""

class Solution:
    def intersection(self, nums1: list, nums2: list) -> list:
        max_list = nums1 if len(nums1) > len(nums2) else nums2
        min_list = nums1 if len(nums1) < len(nums2) else nums2
        intersection = []

        for val in min_list:
            if val in max_list and val not in intersection:   # x in y - time for lists is O(n)
                intersection.append(val)

        return intersection
