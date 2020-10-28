from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        result = []
        if nums:
            start, end = 0, 1
            for end in range(end, n):
                if nums[end] - nums[end - 1] != 1:
                    result.append(self.__get_range(nums, start, end))
                    start = end

            result.append(self.__get_range(nums, start, n))

        return result

    def __get_range(self, nums: List[int], start: int, end: int) -> str:
        if start != end - 1:
            return "%d->%d" % (nums[start], nums[end - 1])
        return "%d" % nums[start]


(Solution()).summaryRanges([0,2,3,4,6,8,9])
# [0,1,2,4,5,7]
# [0,2,3,4,6,8,9]
# []
# [-1]
# [0]
