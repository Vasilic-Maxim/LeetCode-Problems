class Solution:
    """
    n - len(max_list)
    m - len(min_list)
    Time: O(m)
    Space: O(m)
    """

    def intersection(self, nums1: list, nums2: list) -> set:
        return set(nums1) & set(nums2)
