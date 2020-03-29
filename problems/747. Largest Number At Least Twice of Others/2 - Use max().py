class Solution(object):
    """
    Time: O(n)
    Space: O(1)
    """

    def dominantIndex(self, nums):
        m = max(nums)

        # Function 'all' require that all the elements
        # of an iterable respect the rule
        if all(m >= 2 * x for x in nums if x != m):
            return nums.index(m)
        return -1
