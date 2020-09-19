from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nums = "_123456789"
        first_digit = int(str(low)[0])
        result = []
        for i in range(len(str(low)), len(str(high)) + 1):
            for j in range(first_digit, 10 - i + 1):
                digit = int(nums[j:j + i])
                if digit > high:
                    break
                if low <= digit:
                    result.append(digit)
            first_digit = 1
        return result
