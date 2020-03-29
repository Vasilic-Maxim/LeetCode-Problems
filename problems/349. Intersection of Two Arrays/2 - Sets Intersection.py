"""
n - len(max_list)
m - len(min_list)
Time: O(m)
Space: O(m)
"""
class Solution:
    def intersection(self, nums1: list, nums2: list) -> list:
        return set(nums1) & set(nums2)
