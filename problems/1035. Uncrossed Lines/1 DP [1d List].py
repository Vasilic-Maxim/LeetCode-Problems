from typing import List


class Solution:
    """
    m - len(nums1)
    n - len(nums2)
    Time: O(m * n)
    Space: O(n)
    """

    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [0] * len(nums2)
        for i in range(len(nums1)):
            prev = 0
            for j in range(len(nums2)):
                tmp = dp[j]
                dp[j] = max(prev + (nums1[i] == nums2[j]), dp[j - 1] if j else 0, dp[j])
                prev = tmp
        return dp[-1]
