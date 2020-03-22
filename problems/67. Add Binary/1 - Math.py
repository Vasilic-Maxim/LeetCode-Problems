'''
Time: O(max(len(a), len(b)))
Space: O(max(len(a), len(b))) - space for 'result' list
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aIdx, bIdx = len(a) - 1, len(b) - 1
        result = []
        toAdd = 0
        while aIdx >= 0 or bIdx >= 0 or toAdd:
            x = int(a[aIdx]) if aIdx >= 0 else 0
            y = int(b[bIdx]) if bIdx >= 0 else 0
            s = x + y + toAdd
            digit = s % 2   # 0 or 1
            toAdd = s // 2  # 0 or 1
            result.append(str(digit))
            aIdx -= 1
            bIdx -= 1
        
        return ''.join(result[::-1])