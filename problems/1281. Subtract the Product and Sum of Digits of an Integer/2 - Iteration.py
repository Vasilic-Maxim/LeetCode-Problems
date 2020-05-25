class Solution:
    """
    Time: O(log (n))
    Space: O(1)
    """

    def subtractProductAndSum(self, num: int) -> int:
        mul, add = 1, 0
        while num:
            num, mod = divmod(num, 10)
            mul *= mod
            add += mod

        return mul - add
