from typing import List


class Solution:
    def longestMountain(self, nums: List[int]) -> int:
        """
        Time: O(n)
        Space: O(1)
        """

        n = len(nums)
        biggest_mountain = explorer = 0
        while explorer + 1 < n:
            # set the starting point of the mountain and find the peek
            start = explorer
            while explorer + 1 < n and nums[explorer] < nums[explorer + 1]:
                explorer += 1

            # set the peek and find the end of the mountain
            peek = explorer
            while explorer + 1 < n and nums[explorer] > nums[explorer + 1]:
                explorer += 1

            # if all points are different the we automatically have a
            # mountain length with length >= 3 that might be considered
            # as the biggest mountain.
            if start != peek != explorer:
                biggest_mountain = max(biggest_mountain, explorer - start + 1)

            # skip all duplicates and start again
            while explorer + 1 < n and nums[explorer] == nums[explorer + 1]:
                explorer += 1

        return biggest_mountain
