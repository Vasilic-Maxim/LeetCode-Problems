class Solution:
    def convertToBase7(self, num: int) -> str:
        if not num:
            return "0"

        is_negative = num < 0
        num = abs(num)
        result = []
        while num:
            result.append(str(num % 7))
            num //= 7

        if is_negative:
            result.append('-')

        return "".join(result[::-1])
