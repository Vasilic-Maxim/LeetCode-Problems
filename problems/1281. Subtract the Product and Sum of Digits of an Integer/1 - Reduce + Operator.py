import operator
from functools import reduce


class Solution:
    """
    Time: O(log (n))
    Space: O(log (n))
    """

    def subtractProductAndSum(self, num: int) -> int:
        nums = list(map(int, str(num)))
        return reduce(operator.mul, nums) - reduce(operator.add, nums)
