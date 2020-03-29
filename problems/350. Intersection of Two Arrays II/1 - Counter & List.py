from collections import Counter

"""
n - len(nums1)
m - len(nums2)
Time: O(n + m)
Space: O(min(n, m))
"""
class Solution:
    def intersect(self, nums1: list, nums2: list) -> list:
        if len(nums1) <= len(nums2):
            return self.map(nums1, nums2)
        else:
            return self.map(nums2, nums1)

    def map(self, nums1: list, nums2: list) -> list:
        counter = Counter(nums1)
        response = []

        for _, val in enumerate(nums2):
            if val in counter and counter[val]:
                response.append(val)
                counter[val] -= 1

        return response
