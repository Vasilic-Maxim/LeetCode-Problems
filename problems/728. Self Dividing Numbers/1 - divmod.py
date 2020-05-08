from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [x for x in range(left, right + 1) if self.is_self_div_num(x)]

    def is_self_div_num(self, num: int):
        div = num
        while div:
            div, mod = divmod(div, 10)
            if not mod or num % mod:
                return False
        return True
