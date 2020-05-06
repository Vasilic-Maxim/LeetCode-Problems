from typing import List


class Solution:
    """
    m - len(nums)
    n - len(queries)
    Time: O(max(m, n))
    Space: O(n)
    """

    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        even_sum = sum(num for num in nums if not num % 2)

        for val, index in queries:
            if not (nums[index] % 2):
                even_sum -= nums[index]

            nums[index] += val

            if not (nums[index] % 2):
                even_sum += nums[index]

            result.append(even_sum)

        return result
