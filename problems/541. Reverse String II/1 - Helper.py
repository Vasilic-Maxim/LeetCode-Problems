class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        charList = list(s)
        
        for i in range(0, len(charList), k*2):
            self.reverse(charList, i, min(i + k - 1, len(charList) - 1))
                
        return "".join(charList)
    
    def reverse(self, chars: list, start: int, end: int):
        while start < end:
            chars[start], chars[end] = chars[end], chars[start]
            start += 1
            end -= 1