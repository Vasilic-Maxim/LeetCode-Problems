class Solution:
    """
    Time: O(n * log (n))
    Space: O(1)
    """

    def __init__(self):
        self.good_nums = {"0", "1", "8"}
        self.rotatable_nums = {"0", "1", "2", "5", "6", "8", "9"}

    def rotatedDigits(self, num: int) -> int:
        return sum(self.is_good_num(i) for i in range(1, num + 1))

    def is_good_num(self, num: int) -> bool:
        num_str = set(str(num))
        return num_str <= self.rotatable_nums and not (num_str <= self.good_nums)
