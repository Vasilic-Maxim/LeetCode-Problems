class Solution:
    def checkValidString(self, string: str) -> bool:
        low = high = 0
        for char in string:
            low += 1 if char == '(' else -1
            high += 1 if char != ')' else -1

            if high < 0:
                break

            low = max(low, 0)

        return low == 0
