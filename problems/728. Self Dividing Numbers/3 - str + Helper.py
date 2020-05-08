from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [x for x in range(left, right + 1) if self.is_self_div_num(x)]

    def is_self_div_num(self, num: int):
        for mod in str(num):
            if not int(mod) or num % int(mod):
                return False
        return True
