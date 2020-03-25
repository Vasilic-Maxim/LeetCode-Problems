'''
Time: O(n)
Space: O(n)
'''
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        charList = list(s)
        
        for i in range(0, len(charList), k*2):
            charList[i:i + k] = charList[i:i + k][::-1]
                
        return "".join(charList)