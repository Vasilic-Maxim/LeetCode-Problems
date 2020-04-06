class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = counter = 0
        for i in s:
            counter = counter + (1 if i == "R" else -1)

            if not counter:
                result += 1

        return result
