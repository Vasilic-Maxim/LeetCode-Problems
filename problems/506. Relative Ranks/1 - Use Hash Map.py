from typing import List


class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        database, medals = {}, {1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal"}
        for i, num in enumerate(sorted(nums, reverse=True), start=1):
            database[num] = str(i) if i not in medals else medals[i]

        return [database[num] for i, num in enumerate(nums)]
