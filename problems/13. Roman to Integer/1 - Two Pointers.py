'''
n - length of the string
Time: O(n)
Space: O(1)
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        DICT = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        slow = fast = len(s) - 1
        result = 0
        
        while fast >= 0:
            sVal = DICT[s[slow]]
            fVal = DICT[s[fast]]
            
            result += -fVal if sVal > fVal else fVal
            slow = slow if sVal > fVal else fast
            fast -= 1
        
        return result