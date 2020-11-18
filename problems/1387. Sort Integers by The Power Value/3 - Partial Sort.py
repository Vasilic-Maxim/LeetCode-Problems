from functools import lru_cache
from random import randint


class Solution(object):
    def getKth(self, lo, hi, k):
        @lru_cache(None)
        def power(n):
            if n == 1:
                return 0

            if n % 2:
                return power(3 * n + 1) + 1

            return power(n // 2) + 1

        nums = [[power(i), i] for i in range(lo, hi + 1)]

        def nth_element(i, j, n):
            if i == j:
                return nums[i][1]
            pivot = randint(i, j)
            nums[pivot], nums[j] = nums[j], nums[pivot]
            c, e = i, j - 1
            while c <= e:
                if nums[c] < nums[j]:
                    c += 1
                else:
                    nums[c], nums[e] = nums[e], nums[c]
                    e -= 1
            nums[c], nums[j] = nums[j], nums[c]
            if c + 1 == n:
                return nums[c][1]
            if c + 1 < n:
                return nth_element(c + 1, j, n)
            return nth_element(i, c - 1, n)

        return nth_element(0, len(nums) - 1, k)
