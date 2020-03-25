'''
All Solutions have same complexities
Time: O(n)
Space: O(1)
'''
'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        start, end = 0, len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
'''
'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        for step in range(len(s)//2):
            s[step], s[len(s)-step-1] = s[len(s)-step-1], s[step]
'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[:][::-1]