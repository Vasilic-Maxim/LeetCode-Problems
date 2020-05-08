from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for num in range(left, right + 1):
            for mod in str(num):
                if not int(mod) or num % int(mod):
                    break
            else:
                result.append(num)
        return result
